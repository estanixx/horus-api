from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .camera_type import CameraType
    from .sensor_type import SensorType
    from .gcp_type import GCPType
    from .automaticparams_type import AutomaticParamsType
    from .measurement_type import MeasurementType

@strawberry.type
class StationType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    alias: str
    elevation: float
    lat: float
    lon: float
    country: str
    state: str
    city: str
    responsible: Optional[str]
    description: Optional[str]

    @strawberry.field
    async def cameras(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CameraType", strawberry.lazy(".camera_type")]]:
        db = info.context["db"]
        from app.services import CameraService
        items, total = await CameraService.get_for_station(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def sensors(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["SensorType", strawberry.lazy(".sensor_type")]]:
        db = info.context["db"]
        from app.services import SensorService
        items, total = await SensorService.get_for_station(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))
        
    @strawberry.field
    async def gcps(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["GCPType", strawberry.lazy(".gcp_type")]]:
        db = info.context["db"]
        from app.services import GCPService
        items, total = await GCPService.get_for_station(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def automatic_params(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["AutomaticParamsType", strawberry.lazy(".automaticparams_type")]]:
        db = info.context["db"]
        from app.services import AutomaticParamsService
        items, total = await AutomaticParamsService.get_for_station(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))
        
    @strawberry.field
    async def measurements(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["MeasurementType", strawberry.lazy(".measurement_type")]]:
        db = info.context["db"]
        from app.services import MeasurementService
        items, total = await MeasurementService.get_for_station(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class StationCreateInput:
    alias: str
    elevation: float
    lat: float
    lon: float
    country: str
    state: str
    city: str
    responsible: Optional[str] = None
    description: Optional[str] = None

@strawberry.input
class StationUpdateInput:
    alias: Optional[str] = None
    elevation: Optional[float] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    responsible: Optional[str] = None
    description: Optional[str] = None