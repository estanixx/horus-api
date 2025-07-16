from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .obliqueimage_type import ObliqueImageType
    from .mergedimage_type import MergedImageType
    from .rectifiedimage_type import RectifiedImageType

@strawberry.type
class ImageTypeType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    name: str
    description: Optional[str]
    
    @strawberry.field
    async def oblique_images(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["ObliqueImageType", strawberry.lazy(".obliqueimage_type")]]:
        db = info.context["db"]
        from app.services import ObliqueImageService
        items, total = await ObliqueImageService.get_for_image_type(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def merged_images(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["MergedImageType", strawberry.lazy(".mergedimage_type")]]:
        db = info.context["db"]
        from app.services import MergedImageService
        items, total = await MergedImageService.get_for_image_type(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def rectified_images(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["RectifiedImageType", strawberry.lazy(".rectifiedimage_type")]]:
        db = info.context["db"]
        from app.services import RectifiedImageService
        items, total = await RectifiedImageService.get_for_image_type(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class ImageTypeCreateInput:
    name: str
    description: Optional[str] = None

@strawberry.input
class ImageTypeUpdateInput:
    name: Optional[str] = None
    description: Optional[str] = None