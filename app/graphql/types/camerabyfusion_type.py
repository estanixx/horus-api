from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion_type import FusionType
    from .camera_type import CameraType

@strawberry.type
class CameraByFusionType:
    fusion_id: int
    camera_id: int
    sequence: int
    created_at: datetime
    updated_at: datetime

    fusion: Annotated["FusionType", strawberry.lazy(".fusion_type")]
    camera: Annotated["CameraType", strawberry.lazy(".camera_type")]

@strawberry.input
class CameraByFusionCreateInput:
    fusion_id: int
    camera_id: int
    sequence: int

@strawberry.input
class CameraByFusionUpdateInput:
    sequence: Optional[int] = None