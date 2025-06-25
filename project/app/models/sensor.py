from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .station import Station
    from .measurementtype import MeasurementType


class Sensor(SQLModel, table=True):
    __tablename__ = "sensor"

    name: str = Field(
        sa_column=Column("name", String, nullable=False),
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
    
    x: float
    y: float
    z: float
    isvirtual: bool
    description: Optional[str] = None

    station_ref: Optional["Station"] = Relationship(back_populates="sensors")
    measurement_types: list["MeasurementType"] = Relationship(back_populates="sensor_ref")

