import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CalibrationParameterType, Connection, Edge, PageInfo
from app.services import CalibrationParameterService

@strawberry.type
class CalibrationParameterQuery:
    @strawberry.field
    async def calibrationParameter(self, info: Info, id: int) -> Optional[CalibrationParameterType]:
        """Fetches a single calibration parameter by its ID."""
        db = info.context["db"]
        item = await CalibrationParameterService.get_by_id(db, param_id=id)
        return CalibrationParameterType(**item.dict()) if item else None

    @strawberry.field
    async def calibrationParameters(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[CalibrationParameterType]:
        """Fetches a paginated list of all calibration parameters."""
        db = info.context["db"]
        items, total = await CalibrationParameterService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def calibrationParameters_by_calibration(self, info: Info, calibration_id: int, skip: int = 0, limit: int = 10) -> Connection[CalibrationParameterType]:
        """Fetches calibration parameters for a specific calibration."""
        db = info.context["db"]
        items, total = await CalibrationParameterService.get_for_calibration(db, calibration_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def calibrationParameter_total(self, info: Info) -> int:
        """Returns the total number of calibration parameters."""
        db = info.context["db"]
        _, total = await CalibrationParameterService.get_all_paginated(db, 0, 0)
        return total