from typing import final

from fastapi import UploadFile, HTTPException
from pandas import pandas as pd
from sqlalchemy import text, select, func
from datetime import date

from ..dto.hotel_consumption import HotelConsumption
from ..dto.hotel_occupation import HotelOccupation
from ..utils.db import get_session
from ..dto.city import City
from ..dto.hotel import Hotel
from ..dto.review import Review
from ..utils.validate_csv import validate_datos_uso_transporte

class Cities:
    @staticmethod
    def get_all_rows():
        session = next(get_session())
        return session.execute(select(City)).scalars().all()

    @staticmethod
    def get_all():
        session = next(get_session())
        db_cities = session.execute(select(City)).scalars().all()
        cities = []
        for city in db_cities:
            cities.append({
                "id": city.id,
                "name": city.name,
                "hotels": city.hotels,
                "services": city.services,
                "touristic_routes": city.touristic_routes
            })
        return cities

    @staticmethod
    def get_hotel_ratings():
        session = next(get_session())

        # Query to get average hotel ratings for each city
        results = session.execute(
            select(City.id, City.name, Hotel.id, Hotel.name, func.coalesce(func.avg(Review.stars), 0))
            .join(Hotel, Hotel.city_id == City.id)
            .outerjoin(Review, Review.hotel_id == Hotel.id)  # Outer join to include hotels without reviews
            .group_by(City.id, City.name, Hotel.id)
        ).all()

        # Process results into structured format
        city_dict = {}
        for city_id, city_name, hotel_id, hotel_name, avg_rating in results:
            if city_id not in city_dict:
                city_dict[city_id] = {
                    "id": city_id,
                    "name": city_name,
                    "hotels": []
                }
            city_dict[city_id]["hotels"].append({
                "hotel_id": hotel_id,
                "hotel_name": hotel_name,
                "average_rating": round(avg_rating, 1)
            })

        return list(city_dict.values())

    @staticmethod
    def get_info(city_name: str, on: date):
        city: City = Cities.find_by_name(city_name)
        if city is None:
            raise HTTPException(status_code=400, detail=f"City {city_name} not found")
        session = next(get_session())
        cities_consumptions = session.execute(
            select(
                City.name,
                HotelConsumption.sustainability_percent,
                func.sum(HotelConsumption.energy_kwh).label("total_energy_kwh"),
                func.avg(HotelConsumption.recycle_percent).label("average_recycle_percent"),
                func.sum(HotelConsumption.waste_kg).label("total_waste_kg"),
                func.sum(HotelConsumption.water_usage_m3).label("total_water_usage_m3"),
                func.avg(HotelOccupation.avg_night_price).label("avg_night_price"),
                func.avg(HotelOccupation.rate_percent).label("occupation_average_percent")
            )
            .join(Hotel, Hotel.city_id == City.id)
            .join(HotelConsumption, HotelConsumption.hotel_id == Hotel.id)
            .join(HotelOccupation, HotelOccupation.hotel_id == Hotel.id)
            .filter(City.id == city.id, HotelConsumption.consumed_on == on)
            .group_by(City.name, HotelConsumption.sustainability_percent)
        ).fetchone()  # fetchone() to get the first result tuple

        # If no result is found
        if cities_consumptions is None:
            raise HTTPException(status_code=404, detail="No sustainability data found for this city on the given date")

        # Extract the values from the tuple
        city_name = cities_consumptions[0]
        sustainability_percent = cities_consumptions[1]
        total_energy_kwh = cities_consumptions[2]
        average_recycle_percent = cities_consumptions[3]
        total_waste_kg = cities_consumptions[4]
        total_water_usage_m3 = cities_consumptions[5]
        avg_night_price = cities_consumptions[6]
        occupation_average_percent = cities_consumptions[7]

        # Return the data as a dictionary
        return {
            "city": city_name,
            "sustainability_percent": round(sustainability_percent, 1),
            "total_energy_kwh": total_energy_kwh,
            "average_recycle_percent": round(average_recycle_percent, 1),
            "total_waste_kg": total_waste_kg,
            "total_water_usage_m3": total_water_usage_m3,
            "avg_night_price": round(avg_night_price, 1),
            "occupation_average_percent": round(occupation_average_percent, 1)
        }

    @staticmethod
    def find_by_name(city_name: str) -> City|None:
        session = next(get_session())
        city = session.query(City).filter(City.name == city_name).scalar()
        if city is None:
            return None
        return city

    @staticmethod
    def import_from_csv(valid_files: dict[str, UploadFile]):
        df = pd.read_csv(valid_files["uso_transporte"].file)
        session = next(get_session())

        insert_cities_sql = """
           INSERT INTO Cities (name)
           VALUES (:name)
           ON DUPLICATE KEY UPDATE name = name;
        """
        insert_cities_data: list[object] = []

        for index, row in df.iterrows():
            # Data validation
            (
                csv_transport_usage_date,
                csv_transport_usage_type,
                csv_transport_usage_num_users,
                csv_transport_usage_avg_trip_time,
                csv_transport_usage_popular_route_from,
                csv_transport_usage_popular_route_to
            ) = validate_datos_uso_transporte(row, index+2)

            # Cities insertion
            insert_cities_data.append({
                "name": csv_transport_usage_popular_route_from
            })
            insert_cities_data.append({
                "name": csv_transport_usage_popular_route_to
            })

        session.execute(text(insert_cities_sql), insert_cities_data)
        session.commit()
