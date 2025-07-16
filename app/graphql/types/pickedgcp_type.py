from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .calibration_type import CalibrationType
    from .gcp_type import GCPType

@strawberry.type
class PickedGCPType:
    calibration_id: int
    gcp_id: int
    u: float
    v: float
    created_at: datetime
    updated_at: datetime

    calibration: Annotated["CalibrationType", strawberry.lazy(".calibration_type")]
    gcp: Annotated["GCPType", strawberry.lazy(".gcp_type")]

@strawberry.input
class PickedGCPCreateInput:
    calibration_id: int
    gcp_id: int
    u: float
    v: float

@strawberry.input
class PickedGCPUpdateInput:
    u: Optional[float] = None
    v: Optional[float] = None