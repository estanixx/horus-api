import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import StationType, Connection, Edge, PageInfo
from app.services import StationService

@strawberry.type
class StationQuery:
    @strawberry.field
    async def station(self, info: Info, id: int) -> Optional[StationType]:
        """Fetches a single station by its ID."""
        db = info.context["db"]
        item = await StationService.get_by_id(db, station_id=id)
        return StationType(**item.dict()) if item else None

    @strawberry.field
    async def stations(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[StationType]:
        """Fetches a paginated list of all stations."""
        db = info.context["db"]
        items, total = await StationService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def station_total(self, info: Info) -> int:
        """Returns the total number of stations."""
        db = info.context["db"]
        _, total = await StationService.get_all_paginated(db, 0, 0)
        return total