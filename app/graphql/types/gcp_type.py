from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .station_type import StationType
    from .pickedgcp_type import PickedGCPType

@strawberry.type
class GCPType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    station_id: int
    name: str
    x: float
    y: float
    z: float
    
    station: Annotated["StationType", strawberry.lazy(".station_type")]
    
    @strawberry.field
    async def picked_gcps(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["PickedGCPType", strawberry.lazy(".pickedgcp_type")]]:
        db = info.context["db"]
        from app.services import PickedGCPService
        items, total = await PickedGCPService.get_for_gcp(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class GCPCreateInput:
    station_id: int
    name: str
    x: float
    y: float
    z: float

@strawberry.input
class GCPUpdateInput:
    station_id: Optional[int] = None
    name: Optional[str] = None
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None