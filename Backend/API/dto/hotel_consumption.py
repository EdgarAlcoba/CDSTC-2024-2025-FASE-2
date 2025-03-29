from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint
from datetime import date

class HotelConsumption(SQLModel, table=True):
    __tablename__ = 'Hotels_Consumption'
    id: int = Field(default=None, primary_key=True)
    consumed_on: date = Field(nullable=False)
    energy_kwh: int = Field(nullable=False)
    waste_kg: int = Field(nullable=False)
    recycle_percent: float = Field(nullable=False)
    water_usage_m3: int = Field(nullable=False)
    sustainability_percent: float = Field(nullable=True, default=None)
    hotel_id: int = Field(foreign_key="Hotels.id", nullable=False)


    hotel: "Hotel" = Relationship(back_populates="consumptions")

    __table_args__ = (UniqueConstraint("consumed_on", "hotel_id"),)