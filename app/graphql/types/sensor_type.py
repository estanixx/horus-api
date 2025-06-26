import strawberry
from typing import Optional

@strawberry.type
class SensorType:
    id: int
    name: str
    x: float
    y: float
    z: float
    isvirtual:bool
    description: Optional[str] = None
    station_id: Optional[int] = None


@strawberry.input
class SensorCreateInput:
    name: str
    x: float
    y: float
    z: float
    isvirtual:bool
    description: Optional[str] = None
    station_id: int


@strawberry.input
class SensorUpdateInput:
    name: Optional[str] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None
    isvirtual:Optional[bool] = None
    description: Optional[str] = None
    station_id: Optional[int] = None