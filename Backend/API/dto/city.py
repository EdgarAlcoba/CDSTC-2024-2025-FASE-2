from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class City(SQLModel, table=True):
    __tablename__ = "Cities"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)

    hotels: List["Hotel"] = Relationship(
        back_populates="city",
        cascade_delete=True
    )

    services: List["Service"] = Relationship(
        back_populates="city",
        cascade_delete=True
    )

    touristic_routes: List["TouristicRoute"] = Relationship(
        back_populates="city",
        cascade_delete=True
    )

    transport_usages_origins: List["TransportUsage"] = Relationship(
        back_populates="origin_city",
        sa_relationship_kwargs={"foreign_keys": "TransportUsage.origin_city_id"},
        cascade_delete=True
    )

    transport_usages_destinations: List["TransportUsage"] = Relationship(
        back_populates="destination_city",
        sa_relationship_kwargs={"foreign_keys": "TransportUsage.destination_city_id"},
        cascade_delete=True
    )