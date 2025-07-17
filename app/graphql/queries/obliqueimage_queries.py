import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ObliqueImageType, Connection, Edge, PageInfo
from app.services import ObliqueImageService

@strawberry.type
class ObliqueImageQuery:
    @strawberry.field
    async def obliqueImage(self, info: Info, id: int) -> Optional[ObliqueImageType]:
        """Fetches a single oblique image by its ID."""
        db = info.context["db"]
        item = await ObliqueImageService.get_by_id(db, image_id=id)
        return ObliqueImageType(**item.dict()) if item else None

    @strawberry.field
    async def obliqueImages(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[ObliqueImageType]:
        """Fetches a paginated list of all oblique images."""
        db = info.context["db"]
        items, total = await ObliqueImageService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def obliqueImages_by_camera(self, info: Info, camera_id: int, skip: int = 0, limit: int = 10) -> Connection[ObliqueImageType]:
        """Fetches oblique images for a specific camera."""
        db = info.context["db"]
        items, total = await ObliqueImageService.get_for_camera(db, camera_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))
    
    @strawberry.field
    async def obliqueImage_count_by_camera(self, info: Info, camera_id: int) -> int:
        """Returns the total count of oblique images for a specific camera."""
        db = info.context["db"]
        _, total = await ObliqueImageService.get_for_camera(db, camera_id, 0, 0)
        return total

    @strawberry.field
    async def obliqueImage_total(self, info: Info) -> int:
        """Returns the total number of oblique images."""
        db = info.context["db"]
        _, total = await ObliqueImageService.get_all_paginated(db, 0, 0)
        return total