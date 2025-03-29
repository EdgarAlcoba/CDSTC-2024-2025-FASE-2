from sqlmodel import Field, SQLModel, Relationship
from typing import List

class Service(SQLModel, table=True):
    __tablename__ = 'Services'
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)
    city_id: int = Field(foreign_key="Cities.id", nullable=False)

    city: "City" = Relationship(back_populates="services")

    reviews: List["Review"] = Relationship(
        back_populates="service",
        cascade_delete=True
    )
