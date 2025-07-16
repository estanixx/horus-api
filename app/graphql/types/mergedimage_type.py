from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion_type import FusionType
    from .imagetype_type import ImageTypeType

@strawberry.type
class MergedImageType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    filename: str
    image_type_id: int
    ismini: bool
    path: str
    timestamp: float
    fusion_id: int

    fusion: Annotated["FusionType", strawberry.lazy(".fusion_type")]
    image_type: Annotated["ImageTypeType", strawberry.lazy(".imagetype_type")]

@strawberry.input
class MergedImageCreateInput:
    filename: str
    image_type_id: int
    ismini: bool
    path: str
    timestamp: float
    fusion_id: int

@strawberry.input
class MergedImageUpdateInput:
    filename: Optional[str] = None
    image_type_id: Optional[int] = None
    ismini: Optional[bool] = None
    path: Optional[str] = None
    timestamp: Optional[float] = None
    fusion_id: Optional[int] = None