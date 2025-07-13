import strawberry
from typing import Optional

if TYPE_CHECKING:
    from .image import ImageType
    from .camera import CameraType


@strawberry.type
class ObliqueImageType:
    id: int 
    camera_id: int
    image_type: Optional["ImageType"] 
    camera: Optional["CameraType"] 


@strawberry.input
class ObliqueImageCreateInput:
    camera_id: int
    image_type: Optional["ImageType"] 
    camera: Optional["CameraType"] 
    
    
@strawberry.input
class ObliqueImageUpdateInput:
    camera_id: Optional[int] = None
    image_type: Optional[str] = None 
    camera: Optional[str] = None 
    
    
