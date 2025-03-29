from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint
from sqlalchemy import Column, Text, SmallInteger, String, Computed


class Review(SQLModel, table=True):
    __tablename__ = 'Reviews'
    id: int = Field(default=None, primary_key=True)
    stars: int = Field(sa_column=Column(SmallInteger, nullable=False))
    comment: str = Field(sa_column=Column(Text, nullable=False))

    # Automatically stores first 500 characters of `comment`
    comment_index: str = Field(
        sa_column=Column(String(500), Computed("LEFT(comment, 500)"), nullable=False)
    )

    hotel_id: int = Field(foreign_key="Hotels.id", nullable=True, default=None)
    service_id: int = Field(foreign_key="Services.id", nullable=True, default=None)
    user_id: int = Field(foreign_key="Users.id", nullable=True, default=None)

    hotel: "Hotel" = Relationship(back_populates="reviews")
    service: "Service" = Relationship(back_populates="reviews")
    user: "User" = Relationship(back_populates="reviews")

    __table_args__ = (
        UniqueConstraint("comment_index", "hotel_id"),
        UniqueConstraint("comment_index", "service_id"),
        UniqueConstraint("comment_index", "user_id"),
    )