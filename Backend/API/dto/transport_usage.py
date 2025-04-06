from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint
from datetime import date

class TransportUsage(SQLModel, table=True):
    __tablename__ = 'Transport_Usages'
    id: int = Field(primary_key=True)
    usage_on: date = Field(nullable=False)
    type: str = Field(nullable=False)
    number_users: int = Field(nullable=False)
    avg_trip_time_min: int = Field(nullable=False)
    origin_city_id: int = Field(foreign_key="Cities.id", nullable=False)
    destination_city_id: int = Field(foreign_key="Cities.id", nullable=False)

    origin_city: "City" = Relationship(
        back_populates="transport_usages_origins",
        sa_relationship_kwargs={"foreign_keys": "TransportUsage.origin_city_id"}
    )
    destination_city: "City" = Relationship(
        back_populates="transport_usages_destinations",
        sa_relationship_kwargs={"foreign_keys": "TransportUsage.destination_city_id"}
    )

    __table_args__ = (
        UniqueConstraint("usage_on", "type", "origin_city_id", "destination_city_id"),
    )