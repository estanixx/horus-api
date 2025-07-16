from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .calibration_type import CalibrationType
    from .calibrationvalue_type import CalibrationValueType

@strawberry.type
class CalibrationParameterType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    calibration_id: int
    name: str

    calibration: Annotated["CalibrationType", strawberry.lazy(".calibration_type")]
    
    @strawberry.field
    async def values(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CalibrationValueType", strawberry.lazy(".calibrationvalue_type")]]:
        db = info.context["db"]
        from app.services import CalibrationValueService
        items, total = await CalibrationValueService.get_for_parameter(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class CalibrationParameterCreateInput:
    calibration_id: int
    name: str

@strawberry.input
class CalibrationParameterUpdateInput:
    calibration_id: Optional[int] = None
    name: Optional[str] = None