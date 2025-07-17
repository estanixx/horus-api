import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CameraType, Connection, Edge, PageInfo
from app.services import CameraService, StationService

@strawberry.type
class CameraQuery:
    @strawberry.field
    async def camera(self, info: Info, id: int) -> Optional[CameraType]:
        """Fetches a single camera by its ID."""
        db = info.context["db"]
        item = await CameraService.get_by_id(db, camera_id=id)
        return CameraType(**item.dict()) if item else None

    @strawberry.field
    async def cameras(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[CameraType]:
        """Fetches a paginated list of all cameras."""
        db = info.context["db"]
        items, total = await CameraService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def cameras_by_station(self, info: Info, station_id: int, skip: int = 0, limit: int = 10) -> Connection[CameraType]:
        """Fetches a paginated list of cameras for a specific station."""
        db = info.context["db"]
        items, total = await CameraService.get_for_station(db, station_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def camera_count_by_station(self, info: Info, station_id: int) -> int:
        """Returns the total number of cameras for a specific station."""
        db = info.context["db"]
        _, total = await CameraService.get_for_station(db, station_id, 0, 0)
        return total

    @strawberry.field
    async def camera_total(self, info: Info) -> int:
        """Returns the total number of cameras."""
        db = info.context["db"]
        _, total = await CameraService.get_all_paginated(db, 0, 0)
        return total