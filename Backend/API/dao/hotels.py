from fastapi import UploadFile, HTTPException
from pandas import pandas as pd
from sqlmodel import select
from sqlalchemy import text, func
import random

from ..utils.db import get_session
from ..utils.validate_csv import validate_datos_sostenibilidad
from ..utils.validate_csv import validate_ocupacion_hostelera
from ..dto.hotel import Hotel
from ..dto.city import City

class Hotels:
    @staticmethod
    def get_all():
        session = next(get_session())
        db_hotels = session.execute(select(Hotel)).scalars().all()
        hotels = []
        for hotel in db_hotels:
            hotels.append({
                "id": hotel.id,
                "name": hotel.name,
                "stars": hotel.stars,
                "city": {
                    "id": hotel.city.id,
                    "name": hotel.city.name
                }
            })
        return hotels

    @staticmethod
    def import_from_csv(valid_files: dict[str, UploadFile]):
        df_sustainability_data = pd.read_csv(valid_files["datos_sostenibilidad"].file)
        df_occupation_data = pd.read_csv(valid_files["ocupacion_hotelera"].file)
        session = next(get_session())

        # Obtain random cities
        random_cities: list[City] = \
            session.exec(select(City).order_by(func.random())).all()

        if len(random_cities) < 1:
            raise HTTPException(status_code=400, detail="You must first add cities in order to add hotels")

        insert_hotels_sql = """
               INSERT INTO Hotels (name, stars, description, cancel_time_limit_h, city_id)
               VALUES (:name, :stars, :description, :cancel_time_hr, :city_id)
               ON DUPLICATE KEY UPDATE name = name;
           """
        insert_hotels_data: list[object] = []

        insert_hotels_consumption_sql = """
              INSERT INTO Hotels_Consumption 
                (consumed_on, energy_kwh, waste_kg, recycle_percent, water_usage_m3, hotel_id)
              VALUES 
                (:consumed_on, :energy_kwh, :waste_kg, :recycle_percent, :water_usage_m3, :hotel_id)
              ON DUPLICATE KEY UPDATE consumed_on = consumed_on, hotel_id = hotel_id;
              """
        insert_hotels_consumption_data: list[object] = []

        insert_hotels_occupation_sql = """
              INSERT INTO Hotels_Occupation
                (occupation_on, rate_percent, confirmed_reservations, cancellations, avg_night_price, hotel_id)
              VALUES 
                (:occupation_on, :rate_percent, :confirmed_reservations, :cancellations, :avg_night_price, :hotel_id)
              ON DUPLICATE KEY UPDATE occupation_on = occupation_on, hotel_id = hotel_id;
            """
        insert_hotels_occupation_data: list[object] = []

        for index, row in df_sustainability_data.iterrows():
            # Data validation
            (
                csv_hotel_name, csv_hotel_date,
                csv_hotel_generated_waste, csv_hotel_recycle_percent,
                csv_hotel_water_usage, csv_hotel_power_kwh
            ) = validate_datos_sostenibilidad(row, index + 2)

            # Hotel insertion
            # TODO Get AI to generate this data
            '''
                This choses a city for the hotel. In case the hotel first name
                is the same as a city it will be added to it.
                If no city has the same first name as the hotel then
                a random city will be assigned to it.
            '''
            city_id: int = random_cities[random.randint(0, len(random_cities) - 1)].id

            csv_hotel_name_split = csv_hotel_name.split(" ")
            for city in random_cities:
                city_name_split = city.name.split(" ")
                if csv_hotel_name_split[0] == city_name_split[0]:
                    city_id = city.id
                    break

            insert_hotels_data.append({
                "name": csv_hotel_name,
                "stars": 0,
                "description": "",
                "cancel_time_hr": None,
                "city_id": city_id
            })

        session.execute(text(insert_hotels_sql), insert_hotels_data)
        session.commit()

        # Obtain inserted hotels ids
        inserted_hotels = [hotel['name'] for hotel in insert_hotels_data]
        hotel_ids = session.query(Hotel.id).filter(Hotel.name.in_(inserted_hotels)).all()
        hotel_name_to_id = {hotel_name: hotel_id for hotel_name, hotel_id in zip(inserted_hotels, hotel_ids)}


        for index, row in df_sustainability_data.iterrows():
            # Data validation
            (
                csv_hotel_name, csv_hotel_date,
                csv_hotel_generated_waste, csv_hotel_recycle_percent,
                csv_hotel_water_usage, csv_hotel_power_kwh
            ) = validate_datos_sostenibilidad(row, index + 2)

            # Hotel consumption insertion
            hotel_id = hotel_name_to_id.get(csv_hotel_name)
            insert_hotels_consumption_data.append({
                "consumed_on": csv_hotel_date,
                "energy_kwh": csv_hotel_power_kwh,
                "waste_kg": csv_hotel_generated_waste,
                "recycle_percent": csv_hotel_recycle_percent,
                "water_usage_m3": csv_hotel_water_usage,
                "hotel_id": hotel_id[0]
            })

        session.execute(text(insert_hotels_consumption_sql), insert_hotels_consumption_data)
        session.commit()

        for index, row in df_occupation_data.iterrows():
            # Data validation
            (
                csv_hotel_name, csv_occupation_on,
                csv_rate_percent, csv_confirmed_reservations,
                csv_cancellations, csv_avg_night_price
            ) = validate_ocupacion_hostelera(row, index + 2)

            # Hotel consumption insertion
            hotel_id = hotel_name_to_id.get(csv_hotel_name)
            insert_hotels_occupation_data.append({
                "occupation_on": csv_occupation_on,
                "rate_percent": csv_rate_percent,
                "confirmed_reservations": csv_confirmed_reservations,
                "cancellations": csv_cancellations,
                "avg_night_price": csv_avg_night_price,
                "hotel_id": hotel_id[0]
            })

        session.execute(text(insert_hotels_occupation_sql), insert_hotels_occupation_data)
        session.commit()