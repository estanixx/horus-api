import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CommonPointType, CommonPointCreateInput, CommonPointUpdateInput
from app.services import CommonPointService, FusionService, CameraService
from app.models import CommonPoint

@strawberry.type
class CommonPointMutation:
    @strawberry.mutation
    async def create_common_point(self, info: Info, input: CommonPointCreateInput) -> CommonPointType:
        """Creates a new common point."""
        db = info.context["db"]
        if not await FusionService.get_by_id(db, fusion_id=input.id_fusion):
            raise ValueError(f"Fusion with ID {input.id_fusion} not found.")
        if not await CameraService.get_by_id(db, camera_id=input.camera_id):
            raise ValueError(f"Camera with ID {input.camera_id} not found.")
            
        new_item = await CommonPointService.create(db, CommonPoint(**input.__dict__))
        return CommonPointType(**new_item.dict())

    @strawberry.mutation
    async def update_common_point(self, info: Info, id_fusion: int, camera_id: int, name: str, input: CommonPointUpdateInput) -> Optional[CommonPointType]:
        """Updates an existing common point by its composite ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await CommonPointService.update(db, id_fusion=id_fusion, camera_id=camera_id, name=name, update_data=update_data)
        if not updated_item:
            raise ValueError(f"CommonPoint with ID ({id_fusion}, {camera_id}, {name}) not found.")
        return CommonPointType(**updated_item.dict())

    @strawberry.mutation
    async def delete_common_point(self, info: Info, id_fusion: int, camera_id: int, name: str) -> CommonPointType:
        """Deletes a common point by its composite ID."""
        db = info.context["db"]
        deleted_item = await CommonPointService.delete(db, id_fusion=id_fusion, camera_id=camera_id, name=name)
        if not deleted_item:
            raise ValueError(f"CommonPoint with ID ({id_fusion}, {camera_id}, {name}) not found.")
        return CommonPointType(**deleted_item.dict())