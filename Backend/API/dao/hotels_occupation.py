from datetime import date
from sqlmodel import select
from sqlalchemy import func

from ..dto.hotel_occupation import HotelOccupation
from ..utils.db import get_session

class HotelsOccupation:
    @staticmethod
    def get_occupations_avg_percent(occupation_on: date) -> float:
        session = next(get_session())
        db_hotels_occupations_avg_percent: float = \
            session.execute(select(func.avg(HotelOccupation.rate_percent)).where(
                HotelOccupation.occupation_on == occupation_on)
            ).scalar_one()
        return db_hotels_occupations_avg_percent

    @staticmethod
    def get_total_cancellations(occupation_on: date) -> int:
        session = next(get_session())
        db_hotels_total_cancellations: int = \
            session.execute(select(func.sum(HotelOccupation.cancellations)).where(
                HotelOccupation.occupation_on == occupation_on)
            ).scalar_one()
        return db_hotels_total_cancellations

    @staticmethod
    def get_average_price(occupation_on: date) -> float:
        session = next(get_session())
        db_hotels_average_price: float = \
            session.execute(select(func.avg(HotelOccupation.avg_night_price)).where(
                HotelOccupation.occupation_on == occupation_on)
            ).scalar_one()
        return db_hotels_average_price