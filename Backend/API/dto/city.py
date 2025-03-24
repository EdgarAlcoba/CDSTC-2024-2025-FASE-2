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