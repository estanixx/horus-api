import strawberry
from typing import List, Optional

from app.graphql.types import CameraType
from app.services.camera_service import CameraService
from sqlmodel.ext.asyncio.session import AsyncSession

@strawberry.type
class CameraQuery:

    @strawberry.field
    async def cameras(self, info) -> List[CameraType]:
        db: AsyncSession = info.context["db"]
        db_cameras = await CameraService(db).get_all_cameras()
        return db_cameras # type: ignore


    @strawberry.field
    async def camera(self, info, id: int) -> Optional[CameraType]:
        db: AsyncSession = info.context["db"]
        db_camera = await CameraService(db).get_camera_by_id(id)
        if not db_camera:
            return None
        return db_camera # type: ignore