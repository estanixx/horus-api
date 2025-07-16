import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CameraByFusionType, Connection, Edge, PageInfo
from app.services import CameraByFusionService

@strawberry.type
class CameraByFusionQuery:
    @strawberry.field
    async def cameraByFusion(self, info: Info, fusion_id: int, camera_id: int) -> Optional[CameraByFusionType]:
        """Fetches a single CameraByFusion by its composite ID."""
        db = info.context["db"]
        item = await CameraByFusionService.get_by_ids(db, fusion_id=fusion_id, camera_id=camera_id)
        return CameraByFusionType(**item.dict()) if item else None

    @strawberry.field
    async def camerasByFusion(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[CameraByFusionType]:
        """Fetches a paginated list of all CameraByFusion entries."""
        db = info.context["db"]
        items, total = await CameraByFusionService.get_all_paginated(db, skip, limit)
        edges = [Edge(node=CameraByFusionType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def camerasByFusion_by_fusion(self, info: Info, fusion_id: int, skip: int = 0, limit: int = 10) -> Connection[CameraByFusionType]:
        """Fetches CameraByFusion entries for a specific fusion."""
        db = info.context["db"]
        items, total = await CameraByFusionService.get_for_fusion(db, fusion_id, skip, limit)
        edges = [Edge(node=CameraByFusionType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def camerasByFusion_by_camera(self, info: Info, camera_id: int, skip: int = 0, limit: int = 10) -> Connection[CameraByFusionType]:
        """Fetches CameraByFusion entries for a specific camera."""
        db = info.context["db"]
        items, total = await CameraByFusionService.get_for_camera(db, camera_id, skip, limit)
        edges = [Edge(node=CameraByFusionType(**item.dict()), cursor=str(skip + i)) for i, item in enumerate(items)]
        return Connection(total_count=total, edges=edges, page_info=PageInfo.from_skip_limit(skip, limit, total))

    @strawberry.field
    async def cameraByFusion_total(self, info: Info) -> int:
        """Returns the total number of CameraByFusion entries."""
        db = info.context["db"]
        _, total = await CameraByFusionService.get_all_paginated(db, 0, 0)
        return total