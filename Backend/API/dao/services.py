from fastapi import UploadFile, HTTPException
from pandas import pandas as pd
from sqlmodel import select
from sqlalchemy import text, func
import random

from ..utils.validate_csv import validate_opiniones_turisticas
from ..utils.db import get_session
from ..dto.city import City
from ..dto.service import Service

class Services:
    @staticmethod
    def get_all():
        session = next(get_session())
        db_services = session.execute(select(Service)).scalars().all()
        services = []
        for service in db_services:
            services.append({
                "id": service.id,
                "name": service.name,
                "city": {
                    "id": service.city.id,
                    "name": service.city.name
                }
            })
        return services


    @staticmethod
    def import_from_csv(valid_files: dict[str, UploadFile]):
        df_reviews = pd.read_csv(valid_files["opiniones_turisticas"].file)
        session = next(get_session())

        insert_services_sql = """
           INSERT INTO Services (name, city_id)
           VALUES (:name, :city_id)
           ON DUPLICATE KEY UPDATE name = name;
       """
        insert_services_data: list[object] = []

        # Obtain random cities
        random_cities: list[City] = \
            session.exec(select(City).order_by(func.random())).all()

        if len(random_cities) < 1:
            raise HTTPException(status_code=400, detail="You must first add cities in order to add hotels")

        for index, row in df_reviews.iterrows():
            # Data validation
            (
                csv_review_date, csv_service_type,
                csv_service_name, csv_stars,
                csv_review
            ) = validate_opiniones_turisticas(row, index + 2)

            if csv_service_type != 'Servicio':
                continue

            random_city_id: int = random_cities[random.randint(0, len(random_cities) - 1)].id

            insert_services_data.append({
                "name": csv_service_name,
                "city_id": random_city_id
            })

        session.execute(text(insert_services_sql), insert_services_data)
        session.commit()