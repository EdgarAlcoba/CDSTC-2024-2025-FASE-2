from fastapi import UploadFile, HTTPException
from pandas import pandas as pd
from sqlmodel import select
from sqlalchemy import text
import random

from ..dto import service
from ..utils.validate_csv import validate_opiniones_turisticas
from ..utils.db import get_session
from ..dto.city import City
from ..dto.hotel import Hotel
from ..dto.service import Service
from ..dto.user import User
from ..dao.users import Users

class Reviews:
    @staticmethod
    def import_from_csv(valid_files: dict[str, UploadFile]):
        opiniones_turisticas_file = valid_files["opiniones_turisticas"].file
        opiniones_turisticas_file.seek(0)
        df_reviews = pd.read_csv(opiniones_turisticas_file)
        session = next(get_session())

        insert_reviews_sql = """
           INSERT INTO Reviews 
                (stars, comment, hotel_id, service_id, user_id)
           VALUES 
                (:stars, :comment, :hotel_id, :service_id, :user_id)
           ON DUPLICATE KEY UPDATE 
                comment = VALUES(comment), hotel_id = VALUES(hotel_id), service_id = VALUES(service_id);
       """
        insert_reviews_data: list[object] = []

        # Obtain all hotels
        db_hotels: list[Hotel] = \
            session.exec(select(Hotel)).all()

        # Obtain all services
        db_services: list[Service] = \
            session.exec(select(Service)).all()

        # Obtain random mock users
        comments_per_user = 400
        random_users: list[User] = \
            Users.generate_random(len(df_reviews), comments_per_user)

        # TODO Obtain all routes

        if len(db_hotels) < 1:
            raise HTTPException(status_code=400, detail="You must first add hotels in order to add reviews")
        if len(db_services) < 1:
            raise HTTPException(status_code=400, detail="You must first add services in order to add reviews")

        for index, row in df_reviews.iterrows():
            # Data validation
            (
                csv_review_date, csv_service_type,
                csv_service_name, csv_stars,
                csv_review
            ) = validate_opiniones_turisticas(row, index + 2)


            service_id = None
            hotel_id = None

            if csv_service_type == 'Servicio':
                # Find service
                for db_service in db_services:
                    if db_service.name == csv_service_name:
                        service_id = db_service.id
                        break
                if service_id is None:
                    raise HTTPException(
                        status_code=400,
                        detail=f"You tried to add reviews for an unknown service with name {csv_service_name}"
                    )

            if csv_service_type == 'Hotel':
                # Find hotel
                for db_hotel in db_hotels:
                    if db_hotel.name == csv_service_name:
                        hotel_id = db_hotel.id
                        break
                if hotel_id is None:
                    raise HTTPException(
                        status_code=400,
                        detail=f"You tried to add reviews for an unknown hotel with name {csv_service_name}"
                    )

            insert_reviews_data.append({
                "stars": csv_stars,
                "comment": csv_review,
                "hotel_id": hotel_id,
                "service_id": service_id,
                "user_id": random_users[random.randint(0, len(random_users)-1)].id
            })

            # TODO add route


        session.execute(text(insert_reviews_sql), insert_reviews_data)
        session.commit()

