import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CalibrationValueType, Connection, Edge, PageInfo
from app.services import CalibrationValueService

@strawberry.type
class CalibrationValueQuery:
    @strawberry.field
    async def calibrationValue(self, info: Info, id_param: int, id_col: int, id_row: int) -> Optional[CalibrationValueType]:
        """Fetches a single calibration value by its composite ID."""
        db = info.context["db"]
        item = await CalibrationValueService.get_by_ids(db, id_param=id_param, id_col=id_col, id_row=id_row)
        return CalibrationValueType(**item.dict()) if item else None

    @strawberry.field
    async def calibrationValues(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[CalibrationValueType]:
        """Fetches a paginated list of all calibration values."""
        db = info.context["db"]
        items, total = await CalibrationValueService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=CalibrationValueType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def calibrationValues_by_parameter(self, info: Info, id_param: int, skip: int = 0, limit: int = 10) -> Connection[CalibrationValueType]:
        """Fetches calibration values for a specific calibration parameter."""
        db = info.context["db"]
        items, total = await CalibrationValueService.get_for_parameter(db, id_param, skip, limit)
        edges = [Edge(node=CalibrationValueType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def calibrationValue_total(self, info: Info) -> int:
        """Returns the total number of calibration values."""
        db = info.context["db"]
        _, total = await CalibrationValueService.get_all_paginated(db, 0, 0)
        return total