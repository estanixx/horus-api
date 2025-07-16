from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .camera_type import CameraType

@strawberry.type
class TimeStackType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    filename: str
    camera_id: Optional[int]
    inittime: float
    path: str
    fps: float
    numFrames: int

    camera: Optional[Annotated["CameraType", strawberry.lazy(".camera_type")]]

@strawberry.input
class TimeStackCreateInput:
    filename: str
    inittime: float
    path: str
    fps: float
    numFrames: int
    camera_id: Optional[int] = None

@strawberry.input
class TimeStackUpdateInput:
    camera_id: Optional[int] = None
    inittime: Optional[float] = None
    path: Optional[str] = None
    fps: Optional[float] = None
    numFrames: Optional[int] = None