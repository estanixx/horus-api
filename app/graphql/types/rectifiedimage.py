import strawberry
from typing import Optional

@strawberry.type
class RectifiedImageType:
    id: int
    calibration_id: int
   

@strawberry.input
class RectifiedImageCreateInput:
    image_id: int
    calibration_id: int
    
    
@strawberry.input
class RectifiedImageUpdateInput:
    calibration_id: Optional[int]