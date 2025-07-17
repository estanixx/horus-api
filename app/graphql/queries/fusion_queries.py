import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import FusionType, Connection, Edge, PageInfo
from app.services import FusionService

@strawberry.type
class FusionQuery:
    @strawberry.field
    async def fusion(self, info: Info, id: int) -> Optional[FusionType]:
        """Fetches a single fusion by its ID."""
        db = info.context["db"]
        item = await FusionService.get_by_id(db, fusion_id=id)
        return FusionType(**item.dict()) if item else None

    @strawberry.field
    async def fusions(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[FusionType]:
        """Fetches a paginated list of all fusions."""
        db = info.context["db"]
        items, total = await FusionService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def fusion_total(self, info: Info) -> int:
        """Returns the total number of fusions."""
        db = info.context["db"]
        _, total = await FusionService.get_all_paginated(db, 0, 0)
        return total