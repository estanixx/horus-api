import strawberry
from typing import Optional

@strawberry.type
class CameraType:
    id: int
    reference: str
    sizeX: int
    sizeY: int
    station_id: Optional[int] = None


@strawberry.input
class CameraCreateInput:
    reference: str
    sizeX: int
    sizeY: int
    station_id: int


@strawberry.input
class CameraUpdateInput:
    reference: Optional[str] = None
    sizeX: Optional[int] = None
    sizeY: Optional[int] = None
    station_id: Optional[int] = None