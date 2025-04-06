from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint
from datetime import date

class HotelOccupation(SQLModel, table=True):
    __tablename__ = 'Hotels_Occupation'
    id: int = Field(default=None, primary_key=True)
    occupation_on: date = Field(nullable=False)
    rate_percent: int = Field(nullable=False)
    confirmed_reservations: int = Field(nullable=False)
    cancellations: int = Field(nullable=False)
    avg_night_price: float = Field(nullable=False)
    hotel_id: int = Field(foreign_key="Hotels.id", nullable=False)

    hotel: "Hotel" = Relationship(back_populates="occupations")

    __table_args__ = (UniqueConstraint("occupation_on", "hotel_id"),)