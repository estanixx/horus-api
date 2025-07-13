import strawberry
from typing import Optional

@strawberry.type
class MergedImageType:
    id: int
    fusion_id: int
    
    
@strawberry.input
class MergedImageCreateInput:
    fusion_id: int
    
    
@strawberry.input
class MergedImageUpdateInput:
    fusion_id: Optional[int] = None