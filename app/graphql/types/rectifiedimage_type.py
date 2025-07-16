from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .calibration_type import CalibrationType
    from .imagetype_type import ImageTypeType

@strawberry.type
class RectifiedImageType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    filename: str
    image_type_id: int
    ismini: bool
    path: str
    timestamp: float
    calibration_id: Optional[int]

    calibration: Optional[Annotated["CalibrationType", strawberry.lazy(".calibration_type")]]
    image_type: Annotated["ImageTypeType", strawberry.lazy(".imagetype_type")]

@strawberry.input
class RectifiedImageCreateInput:
    filename: str
    image_type_id: int
    ismini: bool
    path: str
    timestamp: float
    calibration_id: Optional[int] = None

@strawberry.input
class RectifiedImageUpdateInput:
    filename: Optional[str] = None
    image_type_id: Optional[int] = None
    ismini: Optional[bool] = None
    path: Optional[str] = None
    timestamp: Optional[float] = None
    calibration_id: Optional[int] = None