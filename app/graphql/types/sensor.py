from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING
if TYPE_CHECKING:
    from .station import StationType

@strawberry.type
class SensorType:
    """GraphQL type for the Sensor model."""
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    name: str
    station_id: int
    x: float
    y: float
    z: float
    is_virtual: bool
    description: Optional[str]
    station: Annotated["StationType", strawberry.lazy(".station")]

@strawberry.input
class SensorCreateInput:
    """GraphQL input type for creating a new Sensor."""
    name: str
    station_id: int
    x: float
    y: float
    z: float
    is_virtual: bool = False
    description: Optional[str] = None

@strawberry.input
class SensorUpdateInput:
    """GraphQL input type for updating an existing Sensor."""
    name: Optional[str] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    is_virtual: Optional[bool] = None
    description: Optional[str] = None