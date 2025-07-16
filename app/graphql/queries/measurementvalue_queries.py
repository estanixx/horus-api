import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MeasurementValueType, Connection, Edge, PageInfo
from app.services import MeasurementValueService

@strawberry.type
class MeasurementValueQuery:
    @strawberry.field
    async def measurementValue(self, info: Info, measurement_id: int, id_col: int, id_row: int, id_depth: int) -> Optional[MeasurementValueType]:
        """Fetches a single measurement value by its composite ID."""
        db = info.context["db"]
        item = await MeasurementValueService.get_by_ids(db, measurement_id=measurement_id, id_col=id_col, id_row=id_row, id_depth=id_depth)
        return MeasurementValueType(**item.dict()) if item else None

    @strawberry.field
    async def measurementValues(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[MeasurementValueType]:
        """Fetches a paginated list of all measurement values."""
        db = info.context["db"]
        items, total = await MeasurementValueService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=MeasurementValueType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def measurementValues_by_measurement(self, info: Info, measurement_id: int, skip: int = 0, limit: int = 10) -> Connection[MeasurementValueType]:
        """Fetches values for a specific measurement."""
        db = info.context["db"]
        items, total = await MeasurementValueService.get_for_measurement(db, measurement_id, skip, limit)
        edges = [Edge(node=MeasurementValueType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def measurementValue_total(self, info: Info) -> int:
        """Returns the total number of measurement values."""
        db = info.context["db"]
        _, total = await MeasurementValueService.get_all_paginated(db, 0, 0)
        return total