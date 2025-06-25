<<<<<<< HEAD:project/app/models/sensor.py
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

=======
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from app.models.station import Station

class Sensor(BaseSQLModel, table=True):
    name: str = Field(
        unique=True,
        index=True,
        description="Unique sensor name"
    )
    station_id: str = Field(
        foreign_key="station.id",
        description="id of the associated station"
    )
    x: float = Field(description="Sensor X coordinate")
    y: float = Field(description="Sensor Y coordinate")
    z: float = Field(description="Sensor Z coordinate")
    isvirtual: bool = Field(description="Indicates whether the sensor is virtual")
    description: Optional[str] = Field(
        default=None,
        description="Optional sensor description"
    )

    station: Optional["Station"] = Relationship(back_populates="sensors")
    
    def __repr__(self):
        return f"Sensor(id={self.id}, name='{self.name}', description='{self.description}')"
>>>>>>> main:app/models/sensor.py
