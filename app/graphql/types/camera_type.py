from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .station_type import StationType
    from .obliqueimage_type import ObliqueImageType
    from .calibration_type import CalibrationType
    from .camerabyfusion_type import CameraByFusionType
    from .commonpoint_type import CommonPointType
    from .timestack_type import TimeStackType

@strawberry.type
class CameraType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    station_id: int
    reference: str
    sizeX: int
    sizeY: int
    
    
    station: Annotated["StationType", strawberry.lazy(".station_type")]

    @strawberry.field
    async def oblique_images(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["ObliqueImageType", strawberry.lazy(".obliqueimage_type")]]:
        db = info.context["db"]
        from app.services import ObliqueImageService
        items, total = await ObliqueImageService.get_for_camera(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def calibrations(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CalibrationType", strawberry.lazy(".calibration_type")]]:
        db = info.context["db"]
        from app.services import CalibrationService
        items, total = await CalibrationService.get_for_camera(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))
        
    @strawberry.field
    async def fusions(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CameraByFusionType", strawberry.lazy(".camerabyfusion_type")]]:
        db = info.context["db"]
        from app.services import CameraByFusionService
        items, total = await CameraByFusionService.get_for_camera(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def common_points(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CommonPointType", strawberry.lazy(".commonpoint_type")]]:
        db = info.context["db"]
        from app.services import CommonPointService
        items, total = await CommonPointService.get_for_camera(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def timestacks(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["TimeStackType", strawberry.lazy(".timestack_type")]]:
        db = info.context["db"]
        from app.services import TimeStackService
        items, total = await TimeStackService.get_for_camera(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class CameraCreateInput:
    station_id: int
    alias: str
    port: int
    rtsp_url: str
    description: Optional[str] = None

@strawberry.input
class CameraUpdateInput:
    station_id: Optional[int] = None
    alias: Optional[str] = None
    port: Optional[int] = None
    rtsp_url: Optional[str] = None
    description: Optional[str] = None