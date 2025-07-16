from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .fusion_type import FusionType
    from .fusionvalue_type import FusionValueType

@strawberry.type
class FusionParameterType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    id_fusion: int
    name: str

    fusion: Annotated["FusionType", strawberry.lazy(".fusion_type")]
    
    @strawberry.field
    async def values(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["FusionValueType", strawberry.lazy(".fusionvalue_type")]]:
        db = info.context["db"]
        from app.services import FusionValueService
        items, total = await FusionValueService.get_for_parameter(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class FusionParameterCreateInput:
    id_fusion: int
    name: str

@strawberry.input
class FusionParameterUpdateInput:
    id_fusion: Optional[int] = None
    name: Optional[str] = None