from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .camerabyfusion_type import CameraByFusionType
    from .fusionparameter_type import FusionParameterType
    from .mergedimage_type import MergedImageType
    from .commonpoint_type import CommonPointType

@strawberry.type
class FusionType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    timestamp: float
    fusion_type: str
    
    @strawberry.field
    async def cameras(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CameraByFusionType", strawberry.lazy(".camerabyfusion_type")]]:
        db = info.context["db"]
        from app.services import CameraByFusionService
        items, total = await CameraByFusionService.get_for_fusion(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def parameters(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["FusionParameterType", strawberry.lazy(".fusionparameter_type")]]:
        db = info.context["db"]
        from app.services import FusionParameterService
        items, total = await FusionParameterService.get_for_fusion(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def merged_images(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["MergedImageType", strawberry.lazy(".mergedimage_type")]]:
        db = info.context["db"]
        from app.services import MergedImageService
        items, total = await MergedImageService.get_for_fusion(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def common_points(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CommonPointType", strawberry.lazy(".commonpoint_type")]]:
        db = info.context["db"]
        from app.services import CommonPointService
        items, total = await CommonPointService.get_for_fusion(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class FusionCreateInput:
    timestamp: float
    fusion_type: str

@strawberry.input
class FusionUpdateInput:
    timestamp: Optional[float] = None
    fusion_type: Optional[str] = None