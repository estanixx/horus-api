import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import TimeStackType, Connection, Edge, PageInfo
from app.services import TimeStackService

@strawberry.type
class TimeStackQuery:
    @strawberry.field
    async def timeStack(self, info: Info, filename: str) -> Optional[TimeStackType]:
        """Fetches a single timestack by its filename."""
        db = info.context["db"]
        item = await TimeStackService.get_by_id(db, filename=filename)
        return TimeStackType(**item.dict()) if item else None

    @strawberry.field
    async def timeStacks(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[TimeStackType]:
        """Fetches a paginated list of all timestacks."""
        db = info.context["db"]
        items, total = await TimeStackService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def timeStacks_by_camera(self, info: Info, camera_id: int, skip: int = 0, limit: int = 10) -> Connection[TimeStackType]:
        """Fetches timestacks for a specific camera."""
        db = info.context["db"]
        items, total = await TimeStackService.get_for_camera(db, camera_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def timeStack_total(self, info: Info) -> int:
        """Returns the total number of timestacks."""
        db = info.context["db"]
        _, total = await TimeStackService.get_all_paginated(db, 0, 0)
        return total