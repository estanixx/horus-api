import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ROIType, Connection, Edge, PageInfo
from app.services import ROIService

@strawberry.type
class ROIQuery:
    @strawberry.field
    async def roi(self, info: Info, id: int) -> Optional[ROIType]:
        """Fetches a single ROI by its ID."""
        db = info.context["db"]
        item = await ROIService.get_by_id(db, roi_id=id)
        return ROIType(**item.dict()) if item else None

    @strawberry.field
    async def rois(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[ROIType]:
        """Fetches a paginated list of all ROIs."""
        db = info.context["db"]
        items, total = await ROIService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=ROIType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def rois_by_calibration(self, info: Info, calibration_id: int, skip: int = 0, limit: int = 10) -> Connection[ROIType]:
        """Fetches ROIs for a specific calibration."""
        db = info.context["db"]
        items, total = await ROIService.get_for_calibration(db, calibration_id, skip, limit)
        edges = [Edge(node=ROIType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def roi_total(self, info: Info) -> int:
        """Returns the total number of ROIs."""
        db = info.context["db"]
        _, total = await ROIService.get_all_paginated(db, 0, 0)
        return total