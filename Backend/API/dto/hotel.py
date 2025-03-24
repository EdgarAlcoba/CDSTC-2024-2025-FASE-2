from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class Hotel(SQLModel, table=True):
    __tablename__ = "Hotels"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False, unique=True)
    stars: int = Field(default=0, nullable=False)
    description: str = Field(nullable=False)
    cancel_time_limit_h: Optional[int] = Field(default=None)
    city_id: int = Field(foreign_key="Cities.id", nullable=False)

    city: "City" = Relationship(back_populates="hotels")

    consumptions: List["HotelConsumption"] = Relationship(
        back_populates="hotel",
        cascade_delete=True
    )

    occupations: List["HotelOccupation"] = Relationship(
        back_populates="hotel",
        cascade_delete=True
    )

    reviews: List["Review"] = Relationship(
        back_populates="hotel",
        cascade_delete=True
    )