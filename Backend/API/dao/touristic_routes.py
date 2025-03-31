from fastapi import UploadFile, HTTPException
from pandas import pandas as pd
from sqlalchemy import select, text

from ..dto.city import City
from ..utils.validate_csv import validate_rutas_turisticas
from ..utils.db import get_session

class TouristicRoutes:
    @staticmethod
    def import_from_csv(valid_files: dict[str, UploadFile]):
        rutas_turisticas_turisticas_file = valid_files["rutas_turisticas"].file
        rutas_turisticas_turisticas_file.seek(0)
        df_reviews = pd.read_csv(rutas_turisticas_turisticas_file)
        session = next(get_session())

        insert_touristic_routes_sql = """
            INSERT INTO Touristic_Routes
                (type, length_km, duration_hr, popularity, city_id)
            VALUES 
                (:type, :length_km, :duration_hr, :popularity, :city_id)
           ON DUPLICATE KEY UPDATE
                duration_hr = VALUES(duration_hr), city_id = VALUES(city_id);
       """
        insert_touristic_routes_data: list[object] = []

        # Obtain all cities
        db_cities: list[City] = \
            session.exec(select(City)).scalars().all()

        for index, row in df_reviews.iterrows():
            # Data validation
            (
                csv_route_name, csv_route_type,
                csv_route_length_km, csv_route_duration_hr,
                csv_route_popularity
            ) = validate_rutas_turisticas(row, index + 2)

            city_id = None

            for db_city in db_cities:
                if db_city.name == csv_route_name:
                    city_id = db_city.id
                    break

            if city_id is None:
                raise HTTPException(
                    status_code=404,
                    detail=f"Tried to import route with unknown city {csv_route_name}"
                )

            insert_touristic_routes_data.append({
                "type": csv_route_type,
                "length_km": csv_route_length_km,
                "duration_hr": csv_route_duration_hr,
                "popularity": csv_route_popularity,
                "city_id": city_id
            })

        session.execute(text(insert_touristic_routes_sql), insert_touristic_routes_data)
        session.commit()

