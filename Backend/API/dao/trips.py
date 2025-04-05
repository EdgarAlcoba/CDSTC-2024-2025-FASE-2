from datetime import datetime
from sqlalchemy import select

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
            trip_data["generated_on"] = trip.created_at.strftime("%Y-%m-%d %H:%M:%S")
            trips_return.append(
                trip.data
            )
        return trips_return
