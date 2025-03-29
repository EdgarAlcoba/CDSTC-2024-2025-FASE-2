from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint

class TouristicRoute(SQLModel, table=True):
    __tablename__ = 'Touristic_Routes'
    id: int = Field(default=None, primary_key=True)
    type: str = Field(nullable=False)
    length_km: float = Field(nullable=False)
    duration_hr: float = Field(nullable=False)
    popularity: float = Field(nullable=False)
    city_id: int = Field(foreign_key="Cities.id", nullable=False)

    city: "City" = Relationship(back_populates="touristic_routes")

    __table_args__ = (
        UniqueConstraint("city_id", "duration_hr"),
    )


