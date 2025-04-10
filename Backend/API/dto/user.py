from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class User(SQLModel, table=True):
    __tablename__ = "Users"
    id: int = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    surname: str = Field(nullable=False)
    email: str = Field(nullable=False, unique=True)
    password: str = Field(nullable=False)
    profile_picture: str = Field(nullable=False, default="default_profile_picture.png")
    mock: bool = Field(default=True, nullable=False)
    role: str = Field(nullable=False, default="basic")
    twofactor_master: Optional[str] = Field(default=None, max_length=32)
    twofactor_recovery_codes: Optional[str] = Field(default=None)
    recovery_code: Optional[str] = Field(default=None, max_length=6)

    reviews: List["Review"] = Relationship(
        back_populates="user",
        cascade_delete=True
    )

    trips: List["Trip"] = Relationship(
        back_populates="user",
        cascade_delete=True
    )