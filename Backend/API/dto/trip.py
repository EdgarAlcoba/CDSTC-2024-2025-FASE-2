from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import Column, JSON
from datetime import datetime

class Trip(SQLModel, table=True):
    __tablename__ = "Trips"
    id: int = Field(default=None, primary_key=True)
    data: dict = Field(sa_column=Column(JSON, nullable=False))
    created_at: datetime = Field(default=None, nullable=False)
    user_id: int = Field(foreign_key="Users.id", nullable=False)

    user: "User" = Relationship(back_populates="trips")