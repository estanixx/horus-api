from sqlmodel import Field, Relationship, Column
from sqlalchemy import Integer, String
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .station import Station
    from .pickedgcp import PickedGCP

class GCP(BaseSQLModel, table=True):

    station_id: int = Field(
        foreign_key='station.id',
        sa_column=Column(
            "station_id",
            Integer,
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

