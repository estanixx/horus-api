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
    
    def __repr__(self):
        return f"Sensor(id={self.id}, name='{self.name}', description='{self.description}')"
