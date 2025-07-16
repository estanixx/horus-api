import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ImageTypeType, Connection, Edge, PageInfo
from app.services import ImageTypeService

@strawberry.type
class ImageTypeQuery:
    @strawberry.field
    async def imageType(self, info: Info, id: int) -> Optional[ImageTypeType]:
        """Fetches a single image type by its ID."""
        db = info.context["db"]
        item = await ImageTypeService.get_by_id(db, type_id=id)
        return ImageTypeType(**item.dict()) if item else None

    @strawberry.field
    async def imageTypes(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[ImageTypeType]:
        """Fetches a paginated list of all image types."""
        db = info.context["db"]
        items, total = await ImageTypeService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=ImageTypeType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def imageType_total(self, info: Info) -> int:
        """Returns the total number of image types."""
        db = info.context["db"]
        _, total = await ImageTypeService.get_all_paginated(db, 0, 0)
        return total