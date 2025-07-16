import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MeasurementTypeType, Connection, Edge, PageInfo
from app.services import MeasurementTypeService

@strawberry.type
class MeasurementTypeQuery:
    @strawberry.field
    async def measurementType(self, info: Info, id: int) -> Optional[MeasurementTypeType]:
        """Fetches a single measurement type by its ID."""
        db = info.context["db"]
        item = await MeasurementTypeService.get_by_id(db, type_id=id)
        return MeasurementTypeType(**item.dict()) if item else None

    @strawberry.field
    async def measurementTypes(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[MeasurementTypeType]:
        """Fetches a paginated list of all measurement types."""
        db = info.context["db"]
        items, total = await MeasurementTypeService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=MeasurementTypeType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def measurementTypes_by_sensor(self, info: Info, sensor_id: int, skip: int = 0, limit: int = 10) -> Connection[MeasurementTypeType]:
        """Fetches measurement types for a specific sensor."""
        db = info.context["db"]
        items, total = await MeasurementTypeService.get_for_sensor(db, sensor_id, skip, limit)
        edges = [Edge(node=MeasurementTypeType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def measurementType_total(self, info: Info) -> int:
        """Returns the total number of measurement types."""
        db = info.context["db"]
        _, total = await MeasurementTypeService.get_all_paginated(db, 0, 0)
        return total