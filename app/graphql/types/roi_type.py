from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .calibration_type import CalibrationType
    from .roicoordinate_type import ROICoordinateType

@strawberry.type
class ROIType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    calibration_id: int
    type: str
    timestamp: float

    calibration: Annotated["CalibrationType", strawberry.lazy(".calibration_type")]
    
    @strawberry.field
    async def coordinates(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["ROICoordinateType", strawberry.lazy(".roicoordinate_type")]]:
        db = info.context["db"]
        from app.services import ROICoordinateService
        items, total = await ROICoordinateService.get_for_roi(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class ROICreateInput:
    calibration_id: int
    type: str
    timestamp: float

@strawberry.input
class ROIUpdateInput:
    calibration_id: Optional[int] = None
    type: Optional[str] = None
    timestamp: Optional[float] = None