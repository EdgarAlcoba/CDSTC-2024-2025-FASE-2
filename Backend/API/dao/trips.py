from datetime import datetime
from sqlalchemy import select

from ..dto.user import User
from ..dto.trip import Trip
from ..utils.db import get_session

class Trips:
    @staticmethod
    def get_all_rows():
        session = next(get_session())
        return session.execute(select(Trip)).scalars().all()

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
            weekday = trip.created_at.strftime("%A").capitalize()
            month_name = trip.created_at.strftime("%B").capitalize()
            if weekday == "Monday":
                weekday = "Lunes"
            if weekday == "Tuesday":
                weekday = "Martes"
            if weekday == "Wednesday":
                weekday = "Miércoles"
            if weekday == "Thursday":
                weekday = "Jueves"
            if weekday == "Friday":
                weekday = "Viernes"
            if weekday == "Saturday":
                weekday = "Sábado"
            if weekday == "Sunday":
                weekday = "Domingo"
            if month_name == "January":
                month_name = "Enero"
            if month_name == "Februrary":
                month_name = "Febrero"
            if month_name == "March":
                month_name = "Marzo"
            if month_name == "April":
                month_name = "Abril"
            if month_name == "May":
                month_name = "Mayo"
            if month_name == "Junio":
                month_name = "June"
            if month_name == "July":
                month_name = "Julio"
            if month_name == "August":
                month_name = "Agosto"
            if month_name == "September":
                month_name = "Septiembre"
            if month_name == "October":
                month_name = "Octubre"
            if month_name == "November":
                month_name = "Noviembre"
            if month_name == "December":
                month_name = "Diciembre"
            trip_data["generated_on"] = trip.created_at.strftime(f"{weekday} %-d de {month_name} de %Y")

            trips_return.append(
                trip.data
            )
        return trips_return
