import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ROICoordinateType, Connection, Edge, PageInfo
from app.services import ROICoordinateService

@strawberry.type
class ROICoordinateQuery:
    @strawberry.field
    async def roiCoordinate(self, info: Info, id: int) -> Optional[ROICoordinateType]:
        """Fetches a single ROI coordinate by its ID."""
        db = info.context["db"]
        item = await ROICoordinateService.get_by_id(db, coord_id=id)
        return ROICoordinateType(**item.dict()) if item else None

    @strawberry.field
    async def roiCoordinates(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[ROICoordinateType]:
        """Fetches a paginated list of all ROI coordinates."""
        db = info.context["db"]
        items, total = await ROICoordinateService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=ROICoordinateType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def roiCoordinates_by_roi(self, info: Info, roi_id: int, skip: int = 0, limit: int = 10) -> Connection[ROICoordinateType]:
        """Fetches coordinates for a specific ROI."""
        db = info.context["db"]
        items, total = await ROICoordinateService.get_for_roi(db, roi_id, skip, limit)
        edges = [Edge(node=ROICoordinateType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def roiCoordinate_total(self, info: Info) -> int:
        """Returns the total number of ROI coordinates."""
        db = info.context["db"]
        _, total = await ROICoordinateService.get_all_paginated(db, 0, 0)
        return total