import strawberry
from typing import Optional
from app.graphql.types import CameraType, CameraCreateInput, CameraUpdateInput
from app.models import Camera
from app.services import CameraService
from sqlmodel.ext.asyncio.session import AsyncSession

@strawberry.type
class CameraMutation:

    @strawberry.mutation
    async def create_camera(self, info, input: CameraCreateInput) -> CameraType:
        db: AsyncSession = info.context["db"]
        input_dict = strawberry.asdict(input)
        camera_data = Camera.parse_obj(input_dict)
        camera = await CameraService(db).create_camera(camera_data)
        return camera # type: ignore


    @strawberry.mutation
    async def update_camera(self, info, id: int, input: CameraUpdateInput) -> Optional[CameraType]:
        db: AsyncSession = info.context["db"]
        input_dict = {k: v for k, v in strawberry.asdict(input).items() if v is not None}
        camera_data = Camera.parse_obj(input_dict)
        camera = await CameraService(db).update_camera(id, camera_data)
        return camera  # type: ignore


    @strawberry.mutation
    async def delete_camera(self, info, id: int) -> bool:
        db: AsyncSession = info.context["db"]
        deleted = await CameraService(db).delete_camera(id)
        return deleted