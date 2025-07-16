import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MergedImageType, Connection, Edge, PageInfo
from app.services import MergedImageService

@strawberry.type
class MergedImageQuery:
    @strawberry.field
    async def mergedImage(self, info: Info, id: int) -> Optional[MergedImageType]:
        """Fetches a single merged image by its ID."""
        db = info.context["db"]
        item = await MergedImageService.get_by_id(db, image_id=id)
        return MergedImageType(**item.dict()) if item else None

    @strawberry.field
    async def mergedImages(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[MergedImageType]:
        """Fetches a paginated list of all merged images."""
        db = info.context["db"]
        items, total = await MergedImageService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=MergedImageType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def mergedImages_by_fusion(self, info: Info, fusion_id: int, skip: int = 0, limit: int = 10) -> Connection[MergedImageType]:
        """Fetches merged images for a specific fusion."""
        db = info.context["db"]
        items, total = await MergedImageService.get_for_fusion(db, fusion_id, skip, limit)
        edges = [Edge(node=MergedImageType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))
    
    @strawberry.field
    async def mergedImage_total(self, info: Info) -> int:
        """Returns the total number of merged images."""
        db = info.context["db"]
        _, total = await MergedImageService.get_all_paginated(db, 0, 0)
        return total