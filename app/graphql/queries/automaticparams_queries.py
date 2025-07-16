import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import AutomaticParamsType, Connection, Edge, PageInfo
from app.services import AutomaticParamsService

@strawberry.type
class AutomaticParamsQuery:
    @strawberry.field
    async def automatic_param(self, info: Info, id: int) -> Optional[AutomaticParamsType]:
        """Fetches a single AutomaticParams by its ID."""
        db = info.context["db"]
        item = await AutomaticParamsService.get_by_id(db, param_id=id)
        return AutomaticParamsType(**item.dict()) if item else None

    @strawberry.field
    async def automatic_params(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[AutomaticParamsType]:
        """Fetches a paginated list of all AutomaticParams."""
        db = info.context["db"]
        items, total = await AutomaticParamsService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=AutomaticParamsType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def automatic_params_by_station(self, info: Info, station_id: int, skip: int = 0, limit: int = 10) -> Connection[AutomaticParamsType]:
        """Fetches a paginated list of AutomaticParams for a specific station."""
        db = info.context["db"]
        items, total = await AutomaticParamsService.get_for_station(db, station_id, skip, limit)
        edges = [Edge(node=AutomaticParamsType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def automatic_params_total(self, info: Info) -> int:
        """Returns the total number of AutomaticParams."""
        db = info.context["db"]
        _, total = await AutomaticParamsService.get_all_paginated(db, 0, 0)
        return total