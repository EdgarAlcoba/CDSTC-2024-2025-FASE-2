from sqlmodel import select
from sqlalchemy import func
from datetime import date

from ..dto.hotel import Hotel
from ..dto.city import City
from ..utils.constants import init as get_constants
from ..utils.db import get_session
from ..dto.hotel_consumption import HotelConsumption

class HotelsConsumption:
    @staticmethod
    def get_average_eco_index(consumed_on: date, city_id: int) -> float|None:
        session = next(get_session())
        db_hotels_average_eco_index: float = \
            session.execute(select(func.avg(HotelConsumption.sustainability_percent)).where(
                HotelConsumption.consumed_on == consumed_on)
            ).scalar_one()
        if city_id:
            db_city: City = session.execute(select(City).where(City.id == city_id)).scalar()
            if not db_city:
                return None
            db_hotels_average_eco_index: float = \
                session.execute(select(func.avg(HotelConsumption.sustainability_percent)).where(
                    HotelConsumption.consumed_on == consumed_on and
                    HotelConsumption.hotel.city_id == city_id)
                ).scalar_one()
        return db_hotels_average_eco_index

    @staticmethod
    def get_top_eco_indexes(consumed_on: date, city_id: int = None, top: int = 10) -> list[dict[str, any]]:
        with next(get_session()) as session:
            query = (
                select(Hotel.id, Hotel.name, Hotel.stars, City.id, City.name, HotelConsumption.sustainability_percent)
                .join(HotelConsumption.hotel)
                .join(Hotel.city)
                .where(HotelConsumption.consumed_on == consumed_on)
                .order_by(HotelConsumption.sustainability_percent.desc())
                .limit(top)
            )

            if city_id:
                query = query.where(Hotel.city_id == city_id)

            db_hotels_top_eco_indexes = [
                {
                    "id": id,
                    "name": name,
                    "stars": stars,
                    "city": {
                        "id": city_id if city_id else city_id_db,
                        "name": city_name
                    },
                    "sustainability_percent": sustainability_percent,
                }
                for id, name, stars, city_id_db, city_name, sustainability_percent in session.execute(query).all()
            ]

        return db_hotels_top_eco_indexes



    @staticmethod
    def calculate_sustainability_percent(
        energy_kwh: int, waste_kg: int,
        recycle_percent: float, water_usage_m3: int,
        energy_kwh_max: int, waste_kg_max: int, water_usage_m3_max: int) -> float:
        constants = get_constants()

        energy_converted: float = energy_kwh/energy_kwh_max
        waste_kg_converted: float = waste_kg/waste_kg_max
        water_usage_m3_converted: float = water_usage_m3/water_usage_m3_max
        recycle_percent_converted: float = 1 - (recycle_percent/100)

        sustainability_percent: float = 100 - (
            (constants['SUSTAINABILITY_INDEX_ENERGY_IMPORTANCE'] * energy_converted) +
            (constants['SUSTAINABILITY_INDEX_WASTE_IMPORTANCE'] * waste_kg_converted) +
            (constants['SUSTAINABILITY_INDEX_RECYCLING_IMPORTANCE'] * recycle_percent_converted) +
            (constants['SUSTAINABILITY_INDEX_WATER_USAGE_IMPORTANCE'] * water_usage_m3_converted)
        ) * 100

        return sustainability_percent

    @staticmethod
    def generate_sustainability_indexes():
        # Obtain maximum values
        session = next(get_session())
        query_get_maximums = select(
            func.max(HotelConsumption.energy_kwh),
            func.max(HotelConsumption.waste_kg),
            func.max(HotelConsumption.water_usage_m3)
        )
        maximums_result = session.execute(query_get_maximums).first()
        if len(maximums_result) < 1:
            raise RuntimeWarning('Tried to generate hotels consumption with no hotels consumption data')
        energy_kwh_max = maximums_result[0]
        waste_kg_max = maximums_result[1]
        water_usage_m3_max = maximums_result[2]

        # Get hotels consumptions to compute their indexes
        db_hotels_consumption: list[HotelConsumption] = session.scalars(select(HotelConsumption)).all()

        for db_hotel_consumption in db_hotels_consumption:
            db_hotel_consumption.sustainability_percent = \
                HotelsConsumption.calculate_sustainability_percent(
                    db_hotel_consumption.energy_kwh, db_hotel_consumption.waste_kg,
                    db_hotel_consumption.recycle_percent, db_hotel_consumption.water_usage_m3,
                    energy_kwh_max, waste_kg_max, water_usage_m3_max
                )
        session.commit()