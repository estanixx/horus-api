from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .station_type import StationType

@strawberry.type
class AutomaticParamsType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    station_id: int
    type: str
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int
    step: int
    duration: Optional[int]
    num_images: Optional[int]

    station: Annotated["StationType", strawberry.lazy(".station_type")]

@strawberry.input
class AutomaticParamsCreateInput:
    station_id: int
    type: str
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int
    step: int
    duration: Optional[int] = None
    num_images: Optional[int] = None

@strawberry.input
class AutomaticParamsUpdateInput:
    station_id: Optional[int] = None
    type: Optional[str] = None
    start_hour: Optional[int] = None
    start_minute: Optional[int] = None
    end_hour: Optional[int] = None
    end_minute: Optional[int] = None
    step: Optional[int] = None
    duration: Optional[int] = None
    num_images: Optional[int] = None