import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CalibrationType, Connection, Edge, PageInfo
from app.services import CalibrationService

@strawberry.type
class CalibrationQuery:
    @strawberry.field
    async def calibration(self, info: Info, id: int) -> Optional[CalibrationType]:
        """Fetches a single calibration by its ID."""
        db = info.context["db"]
        item = await CalibrationService.get_by_id(db, calibration_id=id)
        return CalibrationType(**item.dict()) if item else None

    @strawberry.field
    async def calibrations(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[CalibrationType]:
        """Fetches a paginated list of all calibrations."""
        db = info.context["db"]
        items, total = await CalibrationService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def calibrations_by_camera(self, info: Info, camera_id: int, skip: int = 0, limit: int = 10) -> Connection[CalibrationType]:
        """Fetches calibrations for a specific camera."""
        db = info.context["db"]
        items, total = await CalibrationService.get_for_camera(db, camera_id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def calibration_total(self, info: Info) -> int:
        """Returns the total number of calibrations."""
        db = info.context["db"]
        _, total = await CalibrationService.get_all_paginated(db, 0, 0)
        return total