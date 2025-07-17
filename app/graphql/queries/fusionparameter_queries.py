import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import FusionParameterType, Connection, Edge, PageInfo
from app.services import FusionParameterService

@strawberry.type
class FusionParameterQuery:
    @strawberry.field
    async def fusionParameter(self, info: Info, id: int) -> Optional[FusionParameterType]:
        """Fetches a single fusion parameter by its ID."""
        db = info.context["db"]
        item = await FusionParameterService.get_by_id(db, param_id=id)
        return FusionParameterType(**item.dict()) if item else None

    @strawberry.field
    async def fusionParameters(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[FusionParameterType]:
        """Fetches a paginated list of all fusion parameters."""
        db = info.context["db"]
        items, total = await FusionParameterService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def fusionParameters_by_fusion(self, info: Info, fusion_id: int, skip: int = 0, limit: int = 10) -> Connection[FusionParameterType]:
        """Fetches fusion parameters for a specific fusion."""
        db = info.context["db"]
        items, total = await FusionParameterService.get_for_fusion(db, fusion_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def fusionParameter_total(self, info: Info) -> int:
        """Returns the total number of fusion parameters."""
        db = info.context["db"]
        _, total = await FusionParameterService.get_all_paginated(db, 0, 0)
        return total