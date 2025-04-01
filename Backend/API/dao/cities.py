from fastapi import UploadFile
from pandas import pandas as pd
from sqlalchemy.orm import selectinload
from sqlalchemy import text, select, func

from ..utils.db import get_session
from ..dto.city import City
from ..dto.hotel import Hotel
from ..dto.review import Review
from ..utils.validate_csv import validate_datos_uso_transporte

class Cities:
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
