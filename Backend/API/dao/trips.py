from datetime import datetime
from sqlalchemy import select
import locale

from ..dto.user import User
from ..dto.trip import Trip
from ..utils.db import get_session

class Trips:
    @staticmethod
    def add(user: User, raw_trip: object) -> object:
        session = next(get_session())
        trip = Trip(
            data=raw_trip,
            user_id=user.id,
            created_at=datetime.now(),
        )
        session.add(trip)
        session.commit()
        return {
            "id": trip.id,
            "created_at": trip.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def get_all(user: User) -> object:
        session = next(get_session())
        trips: list[Trip] = session.execute(
            select(Trip)
        ).scalars().all()
        trips_return = []
        for trip in trips:
            trip_data = trip.data
            trip_data["id"] = trip.id
            default_locale = locale.getlocale(locale.LC_TIME)
            locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
            weekday = trip.created_at.strftime("%A").capitalize()
            month_name = trip.created_at.strftime("%B").capitalize()
            locale.setlocale(locale.LC_TIME, default_locale)
            trip_data["generated_on"] = trip.created_at.strftime(f"{weekday} %-d de {month_name} de %Y")

            trips_return.append(
                trip.data
            )
        return trips_return
