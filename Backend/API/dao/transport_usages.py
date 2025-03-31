from fastapi import UploadFile, HTTPException
from pandas import pandas as pd
from sqlalchemy import select, text

from ..dto.city import City
from ..utils.db import get_session
from ..utils.validate_csv import validate_datos_uso_transporte


class TransportUsages:
    @staticmethod
    def import_from_csv(valid_files: dict[str, UploadFile]):
        uso_transporte_file = valid_files["uso_transporte"].file
        uso_transporte_file.seek(0)
        df_reviews = pd.read_csv(uso_transporte_file)
        session = next(get_session())

        insert_transport_usages_sql = """
            INSERT INTO Transport_Usages
                (usage_on, type, number_users, avg_trip_time_min, origin_city_id, destination_city_id)
            VALUES 
                (:usage_on, :type, :number_users, :avg_trip_time_min, :origin_city_id, :destination_city_id)
           ON DUPLICATE KEY UPDATE
                usage_on = VALUES(usage_on),
                type = VALUES(type),
                origin_city_id = VALUES(origin_city_id),
                destination_city_id = VALUES(destination_city_id);
       """
        insert_transport_usages_data: list[object] = []

        # Obtain all cities
        db_cities: list[City] = \
            session.exec(select(City)).scalars().all()

        for index, row in df_reviews.iterrows():
            # Data validation
            (
                csv_transport_usage_date,
                csv_transport_usage_type,
                csv_transport_usage_num_users,
                csv_transport_usage_avg_trip_time,
                csv_transport_usage_popular_route_from,
                csv_transport_usage_popular_route_to
            ) = validate_datos_uso_transporte(row, index + 2)

            origin_city_id = None
            destination_city_id = None

            for db_city in db_cities:
                if db_city.name == csv_transport_usage_popular_route_from:
                    origin_city_id = db_city.id
                if db_city.name == csv_transport_usage_popular_route_to:
                    destination_city_id = db_city.id


            if (origin_city_id is None) or (destination_city_id is None):
                raise HTTPException(
                    status_code=400,
                    detail=f"Tried to import transport usage with unknown from city {csv_transport_usage_popular_route_from} or to city {csv_transport_usage_popular_route_to}"
                )

            insert_transport_usages_data.append({
                "usage_on": csv_transport_usage_date,
                "type": csv_transport_usage_type,
                "number_users": csv_transport_usage_num_users,
                "avg_trip_time_min": csv_transport_usage_avg_trip_time,
                "origin_city_id": origin_city_id,
                "destination_city_id": destination_city_id
            })

        session.execute(text(insert_transport_usages_sql), insert_transport_usages_data)
        session.commit()