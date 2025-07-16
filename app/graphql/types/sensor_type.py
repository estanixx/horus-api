from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .station_type import StationType
    from .measurementtype_type import MeasurementTypeType

@strawberry.type
class SensorType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    station_id: int
    alias: str
    type: str
    description: Optional[str]
    
    station: Annotated["StationType", strawberry.lazy(".station_type")]
    
    @strawberry.field
    async def measurement_types(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["MeasurementTypeType", strawberry.lazy(".measurementtype_type")]]:
        db = info.context["db"]
        from app.services import MeasurementTypeService
        items, total = await MeasurementTypeService.get_for_sensor(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class SensorCreateInput:
    station_id: int
    alias: str
    type: str
    description: Optional[str] = None

@strawberry.input
class SensorUpdateInput:
    station_id: Optional[int] = None
    alias: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None