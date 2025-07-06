import strawberry
from typing import Optional

@strawberry.type
class ImageType:
    id: int
    filename: str
    image_type_id: int
    ismini: bool 
    path: str 
    timestamp: float 
    image_type: Optional["ImageType"] = None
    
    
@strawberry.input
class ImageCreateInput:
    filename: str
    image_type_id: int
    ismini: bool 
    path: str 
    timestamp: float 
    image_type: Optional["ImageType"] = None
    
    
@strawberry.input
class ImageUpdateInput:
    filename: Optional[str] = None
    image_type_id: Optional[int] = None
    ismini: Optional[bool] = None
    path: Optional[str] = None
    timestamp: Optional[float] = None
    image_type: Optional["ImageType"] = None
    

    