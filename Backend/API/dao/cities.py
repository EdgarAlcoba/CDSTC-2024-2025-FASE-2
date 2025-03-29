from fastapi import UploadFile
from pandas import pandas as pd
from sqlalchemy import text

from ..utils.db import get_session
from ..utils.validate_csv import validate_datos_uso_transporte

class Cities:
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
