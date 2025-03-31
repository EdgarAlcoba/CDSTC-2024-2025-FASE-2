from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel, select
from passlib.hash import argon2

import os

from ..dto.user import User
from ..dto.city import City
from ..dto.service import Service
from ..dto.hotel import Hotel
from ..dto.review import Review
from ..dto.hotel_consumption import HotelConsumption
from ..dto.hotel_occupation import HotelOccupation
from ..dto.touristic_route import TouristicRoute
from ..dto.transport_usage import TransportUsage
from ..utils.constants import init as get_constants

db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USERNAME')
db_pass = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_port = os.environ.get('DB_PORT')
db_port_int: int = 3306

if db_host is None:
    raise RuntimeError("DB_HOST environment variable is not set")
if db_user is None:
    raise RuntimeError("DB_USERNAME environment variable is not set")
if db_pass is None:
    raise RuntimeError("DB_PASSWORD environment variable is not set")
if db_name is None:
    raise RuntimeError("DB_NAME environment variable is not set")
if db_port is not None:
    try:
        db_port_int = int(db_port)
        if db_port_int < 0 or db_port_int > 65535:
            raise RuntimeError("Database port is not in range of valid ports [0-65535]")
    except ValueError:
        raise RuntimeError("Database port must be an integer")


db_uri = f"mysql+mysqlconnector://{db_user}:{db_pass}@{db_host}:{db_port_int}/{db_name}"

engine = create_engine(db_uri)

def get_session():
    with Session(engine) as session:
        yield session

def create_superadmin():
    session = next(get_session())
    constants = get_constants()
    db_superadmins: list[User] = session.exec(select(User).where(User.email == constants["SUPERADMIN_EMAIL"])).all()
    if len(db_superadmins) < 1:
        session.add(User(
            name="Super",
            surname="Admin",
            email=constants["SUPERADMIN_EMAIL"],
            password=argon2.hash(constants["SUPERADMIN_PASSWORD"]),
            mock=True,
            role="admin"
        ))
        session.commit()


def init_db():
    SQLModel.metadata.create_all(engine)
    create_superadmin()

