from datetime import date, timedelta
from sqlmodel import select
from sqlalchemy import func

from ..dto.hotel import Hotel
from ..dto.city import City
from ..dto.hotel_occupation import HotelOccupation
from ..utils.db import get_session

class HotelsOccupation:
    @staticmethod
    def get_all_rows():
        session = next(get_session())
        return session.execute(select(HotelOccupation)).scalars().all()

    @staticmethod
    def get_occupations_avg_percent(occupation_on: date, city_id: int) -> float|None:
        session = next(get_session())
        db_hotels_occupations_avg_percent: float = \
            session.execute(select(func.avg(HotelOccupation.rate_percent)).where(
                HotelOccupation.occupation_on == occupation_on)
            ).scalar_one()
        if city_id:
            db_city: City = session.execute(select(City).where(City.id == city_id)).scalar()
            if not db_city:
                return None
            db_hotels_occupations_avg_percent: float = \
                session.execute(select(func.avg(HotelOccupation.rate_percent))
                .join(Hotel, HotelOccupation.hotel_id == Hotel.id)
                .where(
                    HotelOccupation.occupation_on == occupation_on,
                    Hotel.city_id == db_city.id)
                ).scalar_one()
        return db_hotels_occupations_avg_percent

    @staticmethod
    def get_total_reservations(occupation_on: date, city_id: int) -> int|None:
        session = next(get_session())
        db_hotels_total_reservations: int = \
            session.execute(select(func.sum(HotelOccupation.confirmed_reservations)).where(
                HotelOccupation.occupation_on == occupation_on)
            ).scalar_one()
        if city_id:
            db_city: City = session.execute(select(City).where(City.id == city_id)).scalar()
            if not db_city:
                return None
            db_hotels_total_reservations: int = \
                session.execute(select(func.sum(HotelOccupation.confirmed_reservations))
                .join(Hotel, HotelOccupation.hotel_id == Hotel.id)
                .where(
                    HotelOccupation.occupation_on == occupation_on,
                    Hotel.city_id == db_city.id)
                ).scalar_one()
        return db_hotels_total_reservations

    @staticmethod
    def get_total_cancellations(occupation_on: date, city_id: int) -> int|None:
        session = next(get_session())
        db_hotels_total_cancellations: int = \
            session.execute(select(func.sum(HotelOccupation.cancellations)).where(
                HotelOccupation.occupation_on == occupation_on)
            ).scalar_one()
        if city_id:
            db_city: City = session.execute(select(City).where(City.id == city_id)).scalar()
            if not db_city:
                return None
            db_hotels_total_cancellations: int = \
                session.execute(select(func.sum(HotelOccupation.cancellations))
                .join(Hotel, HotelOccupation.hotel_id == Hotel.id)
                .where(
                    HotelOccupation.occupation_on == occupation_on,
                    Hotel.city_id == db_city.id)
                ).scalar_one()
        return db_hotels_total_cancellations

    @staticmethod
    def get_average_price(occupation_on: date, city_id: int) -> float|None:
        session = next(get_session())
        db_hotels_average_price: float = \
            session.execute(select(func.avg(HotelOccupation.avg_night_price)).where(
                HotelOccupation.occupation_on == occupation_on)
            ).scalar_one()
        if city_id:
            db_city: City = session.execute(select(City).where(City.id == city_id)).scalar()
            if not db_city:
                return None
            db_hotels_average_price: float = \
                session.execute(select(func.avg(HotelOccupation.avg_night_price))
                .join(Hotel, HotelOccupation.hotel_id == Hotel.id)
                .where(
                    HotelOccupation.occupation_on == occupation_on,
                    Hotel.city_id == db_city.id)
                ).scalar_one()
        return db_hotels_average_price

    @staticmethod
    def get_occupation_days(occupation_on: date, city_id: int, last_days: int = 7) -> list[float]:
        occupation_last_days: list[float] = []
        for i in range(0, last_days):
            hotel_occupation =  HotelsOccupation.get_occupations_avg_percent(
               occupation_on - timedelta(days=i), city_id
            )
            if hotel_occupation is None:
                print(hotel_occupation)
                return []
            occupation_last_days.append(
                hotel_occupation
            )
        return occupation_last_days

    @staticmethod
    def get_average_prices(occupation_on: date, city_id: int, last_days: int = 7) -> list[float]:
        average_prices_last_days: list[float] = []
        for i in range(0, last_days):
            average_price =  HotelsOccupation.get_average_price(
               occupation_on - timedelta(days=i), city_id
            )
            if average_price is None:
                return []
            average_prices_last_days.append(
                average_price
            )
        return average_prices_last_days