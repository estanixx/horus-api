import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CommonPointType, Connection, Edge, PageInfo
from app.services import CommonPointService

@strawberry.type
class CommonPointQuery:
    @strawberry.field
    async def commonPoint(self, info: Info, id_fusion: int, camera_id: int, name: str) -> Optional[CommonPointType]:
        """Fetches a single common point by its composite ID."""
        db = info.context["db"]
        item = await CommonPointService.get_by_ids(db, id_fusion=id_fusion, camera_id=camera_id, name=name)
        return CommonPointType(**item.dict()) if item else None

    @strawberry.field
    async def commonPoints(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[CommonPointType]:
        """Fetches a paginated list of all common points."""
        db = info.context["db"]
        items, total = await CommonPointService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))
    
    @strawberry.field
    async def commonPoints_by_fusion(self, info: Info, fusion_id: int, skip: int = 0, limit: int = 10) -> Connection[CommonPointType]:
        """Fetches common points for a specific fusion."""
        db = info.context["db"]
        items, total = await CommonPointService.get_for_fusion(db, fusion_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def commonPoint_total(self, info: Info) -> int:
        """Returns the total number of common points."""
        db = info.context["db"]
        _, total = await CommonPointService.get_all_paginated(db, 0, 0)
        return total