from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Float, ForeignKey
from typing import Optional, TYPE_CHECKING
from app.models.base import BaseSQLModel
if TYPE_CHECKING:
    from .station import Station
    from .measurementtype import MeasurementType


class Sensor(BaseSQLModel, table=True):
    __tablename__ = "sensor"

    name: str = Field(
        sa_column=Column("name", String, nullable=False),
        unique=True,
        description="Unique sensor name"
    )
    station_id: int = Field(
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
    measurement_types: list["MeasurementType"] = Relationship(back_populates="sensor")

    def __repr__(self):
        return f"Sensor(id={self.id}, name='{self.name}', description='{self.description}')"

