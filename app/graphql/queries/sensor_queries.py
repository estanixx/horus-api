import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import SensorType, Connection, Edge, PageInfo
from app.services import SensorService

@strawberry.type
class SensorQuery:
    @strawberry.field
    async def sensor(self, info: Info, id: int) -> Optional[SensorType]:
        """Fetches a single sensor by its ID."""
        db = info.context["db"]
        item = await SensorService.get_by_id(db, sensor_id=id)
        return SensorType(**item.dict()) if item else None

    @strawberry.field
    async def sensors(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[SensorType]:
        """Fetches a paginated list of all sensors."""
        db = info.context["db"]
        items, total = await SensorService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=SensorType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def sensors_by_station(self, info: Info, station_id: int, skip: int = 0, limit: int = 10) -> Connection[SensorType]:
        """Fetches a paginated list of sensors for a specific station."""
        db = info.context["db"]
        items, total = await SensorService.get_for_station(db, station_id, skip, limit)
        edges = [Edge(node=SensorType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def sensor_count_by_station(self, info: Info, station_id: int) -> int:
        """Returns the total number of sensors for a specific station."""
        db = info.context["db"]
        _, total = await SensorService.get_for_station(db, station_id, 0, 0)
        return total

    @strawberry.field
    async def sensor_total(self, info: Info) -> int:
        """Returns the total number of sensors."""
        db = info.context["db"]
        _, total = await SensorService.get_all_paginated(db, 0, 0)
        return total