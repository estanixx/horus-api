from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Integer, String, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .station import Station
    from .pickedgcp import PickedGCP


class GCP(BaseSQLModel, table=True):
    __tablename__ = "gcp"

    station_id: int = Field(
        sa_column=Column(
            "station_id",
            Integer,
            ForeignKey('station.id'),
            nullable=False,
        )
    )
    name: str = Field(
        sa_column=Column("name", String, nullable=False)
    )

    x: float
    y: float
    z: float

    station: Optional["Station"] = Relationship(back_populates="gcps")
    picked_gcps: list["PickedGCP"] = Relationship(back_populates="gcp")

