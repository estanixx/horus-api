from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .measurementtype_type import MeasurementTypeType
    from .measurementvalue_type import MeasurementValueType
    from .station_type import StationType

@strawberry.type
class MeasurementType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    station_id: int
    measurement_type_id: int
    timestamp: float
    
    station: Annotated["StationType", strawberry.lazy(".station_type")]
    measurement_type: Annotated["MeasurementTypeType", strawberry.lazy(".measurementtype_type")]
    
    @strawberry.field
    async def values(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["MeasurementValueType", strawberry.lazy(".measurementvalue_type")]]:
        db = info.context["db"]
        from app.services import MeasurementValueService
        items, total = await MeasurementValueService.get_for_measurement(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class MeasurementCreateInput:
    station_id: int
    measurement_type_id: int
    timestamp: float

@strawberry.input
class MeasurementUpdateInput:
    station_id: Optional[int] = None
    measurement_type_id: Optional[int] = None
    timestamp: Optional[float] = None