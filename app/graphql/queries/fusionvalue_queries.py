import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import FusionValueType, Connection, Edge, PageInfo
from app.services import FusionValueService

@strawberry.type
class FusionValueQuery:
    @strawberry.field
    async def fusionValue(self, info: Info, matrix_id: int, id_col: int, id_row: int) -> Optional[FusionValueType]:
        """Fetches a single fusion value by its composite ID."""
        db = info.context["db"]
        item = await FusionValueService.get_by_ids(db, matrix_id=matrix_id, id_col=id_col, id_row=id_row)
        return FusionValueType(**item.dict()) if item else None

    @strawberry.field
    async def fusionValues(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[FusionValueType]:
        """Fetches a paginated list of all fusion values."""
        db = info.context["db"]
        items, total = await FusionValueService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def fusionValues_by_parameter(self, info: Info, matrix_id: int, skip: int = 0, limit: int = 10) -> Connection[FusionValueType]:
        """Fetches fusion values for a specific fusion parameter (matrix)."""
        db = info.context["db"]
        items, total = await FusionValueService.get_for_parameter(db, matrix_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def fusionValue_total(self, info: Info) -> int:
        """Returns the total number of fusion values."""
        db = info.context["db"]
        _, total = await FusionValueService.get_all_paginated(db, 0, 0)
        return total