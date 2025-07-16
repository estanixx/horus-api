from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .camera_type import CameraType
    from .imagetype_type import ImageTypeType

@strawberry.type
class ObliqueImageType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    filename: str
    image_type_id: int
    ismini: bool
    path: str
    timestamp: float
    camera_id: int

    camera: Annotated["CameraType", strawberry.lazy(".camera_type")]
    image_type: Annotated["ImageTypeType", strawberry.lazy(".imagetype_type")]

@strawberry.input
class ObliqueImageCreateInput:
    filename: str
    image_type_id: int
    ismini: bool
    path: str
    timestamp: float
    camera_id: int

@strawberry.input
class ObliqueImageUpdateInput:
    filename: Optional[str] = None
    image_type_id: Optional[int] = None
    ismini: Optional[bool] = None
    path: Optional[str] = None
    timestamp: Optional[float] = None
    camera_id: Optional[int] = None