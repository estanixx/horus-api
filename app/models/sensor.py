# app/models/sensor.py

from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .station import Station
    from .measurementtype import MeasurementType

class Sensor(BaseSQLModel, table=True):
    """
    Represents a single sensor device or a virtual sensor point at a station.

    This model stores the sensor's reference name, its physical or virtual coordinates,
    and links to the types of measurements it can produce.

    Attributes:
        id: The primary key for the sensor.
        name: A user-defined name for the sensor (e.g., "Thermometer", "Anemometer").
              This must be unique per station.
        station_id: The foreign key linking this sensor to its parent station.
        x: The X coordinate of the sensor, typically in a local or projected system.
        y: The Y coordinate of the sensor.
        z: The Z coordinate or elevation of the sensor.
        is_virtual: A boolean flag indicating if the sensor is a physical device (False)
                    or a virtual point for data extraction (True).
        description: An optional free-text description of the sensor.
        station: The parent Station object this sensor belongs to.
        measurement_types: A list of MeasurementType objects that this sensor can record.
    """
    __table_args__ = (
        UniqueConstraint("name", "station_id", name="unique_name_per_station"),
    )

    name: str = Field(
        index=True,
        description="Unique sensor name per station."
    )
    station_id: int = Field(
        foreign_key="station.id",
        description="ID of the associated station."
    )
    x: float = Field(description="Sensor X coordinate in a local reference system.")
    y: float = Field(description="Sensor Y coordinate in a local reference system.")
    z: float = Field(description="Sensor Z coordinate (elevation) in a local reference system.")
    is_virtual: bool = Field(default=False, description="Indicates whether the sensor is virtual or physical.")
    description: Optional[str] = Field(
        default=None,
        description="Optional sensor description."
    )

    # --- Relationships ---
    station: "Station" = Relationship(back_populates="sensors")
    measurement_types: List["MeasurementType"] = Relationship(back_populates="sensor")

    def __repr__(self) -> str:
        """Provides a developer-friendly string representation of the Sensor object."""
        return f"Sensor(id={self.id}, name='{self.name}', station_id={self.station_id})"
