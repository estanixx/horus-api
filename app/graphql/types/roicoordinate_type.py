from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .roi_type import ROIType

@strawberry.type
class ROICoordinateType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    roi_id: int
    u: float
    v: float

    roi: Annotated["ROIType", strawberry.lazy(".roi_type")]

@strawberry.input
class ROICoordinateCreateInput:
    roi_id: int
    u: float
    v: float

@strawberry.input
class ROICoordinateUpdateInput:
    roi_id: Optional[int] = None
    u: Optional[float] = None
    v: Optional[float] = None