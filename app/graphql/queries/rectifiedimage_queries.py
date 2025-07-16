import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import RectifiedImageType, Connection, Edge, PageInfo
from app.services import RectifiedImageService

@strawberry.type
class RectifiedImageQuery:
    @strawberry.field
    async def rectifiedImage(self, info: Info, id: int) -> Optional[RectifiedImageType]:
        """Fetches a single rectified image by its ID."""
        db = info.context["db"]
        item = await RectifiedImageService.get_by_id(db, image_id=id)
        return RectifiedImageType(**item.dict()) if item else None

    @strawberry.field
    async def rectifiedImages(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[RectifiedImageType]:
        """Fetches a paginated list of all rectified images."""
        db = info.context["db"]
        items, total = await RectifiedImageService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=RectifiedImageType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def rectifiedImages_by_calibration(self, info: Info, calibration_id: int, skip: int = 0, limit: int = 10) -> Connection[RectifiedImageType]:
        """Fetches rectified images for a specific calibration."""
        db = info.context["db"]
        items, total = await RectifiedImageService.get_for_calibration(db, calibration_id, skip, limit)
        edges = [Edge(node=RectifiedImageType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))
    
    @strawberry.field
    async def rectifiedImage_total(self, info: Info) -> int:
        """Returns the total number of rectified images."""
        db = info.context["db"]
        _, total = await RectifiedImageService.get_all_paginated(db, 0, 0)
        return total