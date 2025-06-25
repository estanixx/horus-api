from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Integer, String, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .station import Station
    from .pickedgcp import PickedGCP


class GCP(SQLModel, table=True):
    __tablename__ = "gcp"

    idgcp: int = Field(
        sa_column=Column("idgcp", Integer, nullable=False),
        primary_key=True
    )

    station: str = Field(
        sa_column=Column(
            "station",
            String,
            ForeignKey("station.name"),
            primary_key=True,
            nullable=False
        )
    )
    name: str = Field(
        sa_column=Column("name", String, nullable=False)
    )

    x: float
    y: float
    z: float

    station_ref: Optional["Station"] = Relationship(back_populates="gcps")
    picked_gcps: list["PickedGCP"] = Relationship(back_populates="gcp")

