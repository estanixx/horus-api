import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CameraType, CameraCreateInput, CameraUpdateInput
from app.services import CameraService, StationService
from app.models import Camera

@strawberry.type
class CameraMutation:
    @strawberry.mutation
    async def create_camera(self, info: Info, input: CameraCreateInput) -> CameraType:
        """Creates a new camera and associates it with a station."""
        db = info.context["db"]
        if not await StationService.get_by_id(db, station_id=input.station_id):
            raise ValueError(f"Station with ID {input.station_id} not found.")
        
        new_item = await CameraService.create(db, Camera(**input.__dict__))
        return CameraType(**new_item.dict())

    @strawberry.mutation
    async def update_camera(self, info: Info, id: int, input: CameraUpdateInput) -> Optional[CameraType]:
        """Updates an existing camera by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await CameraService.update(db, camera_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"Camera with ID {id} not found.")
        return CameraType(**updated_item.dict())

    @strawberry.mutation
    async def delete_camera(self, info: Info, id: int) -> CameraType:
        """Deletes a camera by its ID."""
        db = info.context["db"]
        deleted_item = await CameraService.delete(db, camera_id=id)
        if not deleted_item:
            raise ValueError(f"Camera with ID {id} not found.")
        return CameraType(**deleted_item.dict())