from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion_type import FusionType
    from .camera_type import CameraType

@strawberry.type
class CommonPointType:
    id_fusion: int
    camera_id: int
    name: str
    u: float
    v: float
    created_at: datetime
    updated_at: datetime

    fusion: Annotated["FusionType", strawberry.lazy(".fusion_type")]
    camera: Annotated["CameraType", strawberry.lazy(".camera_type")]

@strawberry.input
class CommonPointCreateInput:
    id_fusion: int
    camera_id: int
    name: str
    u: float
    v: float

@strawberry.input
class CommonPointUpdateInput:
    u: Optional[float] = None
    v: Optional[float] = None