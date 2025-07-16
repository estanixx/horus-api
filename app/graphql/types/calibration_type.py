from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from .common import Connection, Edge, PageInfo

if TYPE_CHECKING:
    from .camera_type import CameraType
    from .rectifiedimage_type import RectifiedImageType
    from .pickedgcp_type import PickedGCPType
    from .calibrationparameter_type import CalibrationParameterType
    from .roi_type import ROIType

@strawberry.type
class CalibrationType:
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    camera_id: int
    timestamp: float
    resolution: float
    EMCuv: Optional[float]
    EMCxy: Optional[float]
    NCE: Optional[float]
    
    camera: Annotated["CameraType", strawberry.lazy(".camera_type")]

    @strawberry.field
    async def rectified_images(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["RectifiedImageType", strawberry.lazy(".rectifiedimage_type")]]:
        db = info.context["db"]
        from app.services import RectifiedImageService
        items, total = await RectifiedImageService.get_for_calibration(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def picked_gcps(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["PickedGCPType", strawberry.lazy(".pickedgcp_type")]]:
        db = info.context["db"]
        from app.services import PickedGCPService
        items, total = await PickedGCPService.get_for_calibration(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def parameters(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["CalibrationParameterType", strawberry.lazy(".calibrationparameter_type")]]:
        db = info.context["db"]
        from app.services import CalibrationParameterService
        items, total = await CalibrationParameterService.get_for_calibration(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def rois(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[Annotated["ROIType", strawberry.lazy(".roi_type")]]:
        db = info.context["db"]
        from app.services import ROIService
        items, total = await ROIService.get_for_calibration(db, self.id, skip, limit)
        edges = [Edge(node=item, cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

@strawberry.input
class CalibrationCreateInput:
    camera_id: int
    timestamp: float
    resolution: float
    EMCuv: Optional[float] = None
    EMCxy: Optional[float] = None
    NCE: Optional[float] = None

@strawberry.input
class CalibrationUpdateInput:
    camera_id: Optional[int] = None
    timestamp: Optional[float] = None
    resolution: Optional[float] = None
    EMCuv: Optional[float] = None
    EMCxy: Optional[float] = None
    NCE: Optional[float] = None