from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint
from sqlalchemy import Column, Text, SmallInteger, func
from datetime import date

class Review(SQLModel, table=True):
    __tablename__ = 'Reviews'
    id: int = Field(default=None, primary_key=True)
    stars: int = Field(sa_column=Column(SmallInteger, nullable=False))
    comment: str = Field(sa_column=Column(Text, nullable=False))
    comment_hash: str = Field(nullable=False)
    published_on: date = Field(nullable=False)
    hotel_id: int = Field(foreign_key="Hotels.id", nullable=True, default=None)
    service_id: int = Field(foreign_key="Services.id", nullable=True, default=None)
    user_id: int = Field(foreign_key="Users.id", nullable=True, default=None)

    hotel: "Hotel" = Relationship(back_populates="reviews")
    service: "Service" = Relationship(back_populates="reviews")
    user: "User" = Relationship(back_populates="reviews")

    __table_args__ = (
        UniqueConstraint("comment_hash", "published_on", "service_id", "stars"),
        UniqueConstraint("comment_hash", "published_on", "hotel_id", "stars")
    )