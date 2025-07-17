import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import GCPType, Connection, Edge, PageInfo
from app.services import GCPService

@strawberry.type
class GCPQuery:
    @strawberry.field
    async def gcp(self, info: Info, id: int) -> Optional[GCPType]:
        """Fetches a single GCP by its ID."""
        db = info.context["db"]
        item = await GCPService.get_by_id(db, gcp_id=id)
        return GCPType(**item.dict()) if item else None

    @strawberry.field
    async def gcps(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[GCPType]:
        """Fetches a paginated list of all GCPs."""
        db = info.context["db"]
        items, total = await GCPService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def gcps_by_station(self, info: Info, station_id: int, skip: int = 0, limit: int = 10) -> Connection[GCPType]:
        """Fetches a paginated list of GCPs for a specific station."""
        db = info.context["db"]
        items, total = await GCPService.get_for_station(db, station_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def gcp_total(self, info: Info) -> int:
        """Returns the total number of GCPs."""
        db = info.context["db"]
        _, total = await GCPService.get_all_paginated(db, 0, 0)
        return total