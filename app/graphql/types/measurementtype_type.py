from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .sensor_type import SensorType
    from .measurement_type import MeasurementType

@strawberry.type
class MeasurementTypeType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    sensor_id: int
    paramname: str
    datatype: str
    unitx: Optional[str]
    unity: Optional[str]
    unitz: Optional[str]
    axisnamex: Optional[str]
    axisnamey: Optional[str]
    axisnamez: Optional[str]
    description: Optional[str]
    
    sensor: Annotated["SensorType", strawberry.lazy(".sensor_type")]
    
    @strawberry.field
    async def measurements(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["MeasurementType", strawberry.lazy(".measurement_type")]]:
        db = info.context["db"]
        from app.services import MeasurementService
        items, total = await MeasurementService.get_for_measurement_type(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class MeasurementTypeCreateInput:
    sensor_id: int
    paramname: str
    datatype: str
    unitx: Optional[str] = None
    unity: Optional[str] = None
    unitz: Optional[str] = None
    axisnamex: Optional[str] = None
    axisnamey: Optional[str] = None
    axisnamez: Optional[str] = None
    description: Optional[str] = None

@strawberry.input
class MeasurementTypeUpdateInput:
    sensor_id: Optional[int] = None
    paramname: Optional[str] = None
    datatype: Optional[str] = None
    unitx: Optional[str] = None
    unity: Optional[str] = None
    unitz: Optional[str] = None
    axisnamex: Optional[str] = None
    axisnamey: Optional[str] = None
    axisnamez: Optional[str] = None
    description: Optional[str] = None