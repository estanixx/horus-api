import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MeasurementType, Connection, Edge, PageInfo
from app.services import MeasurementService

@strawberry.type
class MeasurementQuery:
    @strawberry.field
    async def measurement(self, info: Info, id: int) -> Optional[MeasurementType]:
        """Fetches a single measurement by its ID."""
        db = info.context["db"]
        item = await MeasurementService.get_by_id(db, measurement_id=id)
        return MeasurementType(**item.dict()) if item else None

    @strawberry.field
    async def measurements(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[MeasurementType]:
        """Fetches a paginated list of all measurements."""
        db = info.context["db"]
        items, total = await MeasurementService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def measurements_by_station(self, info: Info, station_id: int, skip: int = 0, limit: int = 10) -> Connection[MeasurementType]:
        """Fetches measurements for a specific station."""
        db = info.context["db"]
        items, total = await MeasurementService.get_for_station(db, station_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def measurements_by_measurement_type(self, info: Info, measurement_type_id: int, skip: int = 0, limit: int = 10) -> Connection[MeasurementType]:
        """Fetches measurements for a specific measurement type."""
        db = info.context["db"]
        items, total = await MeasurementService.get_for_measurement_type(db, measurement_type_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def measurement_total(self, info: Info) -> int:
        """Returns the total number of measurements."""
        db = info.context["db"]
        _, total = await MeasurementService.get_all_paginated(db, 0, 0)
        return total