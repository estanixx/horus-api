import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CameraByFusionType, CameraByFusionCreateInput, CameraByFusionUpdateInput
from app.services import CameraByFusionService, CameraService, FusionService
from app.models import CameraByFusion

@strawberry.type
class CameraByFusionMutation:
    @strawberry.mutation
    async def create_camera_by_fusion(self, info: Info, input: CameraByFusionCreateInput) -> CameraByFusionType:
        """Creates a new CameraByFusion link."""
        db = info.context["db"]
        if not await CameraService.get_by_id(db, camera_id=input.camera_id):
            raise ValueError(f"Camera with ID {input.camera_id} not found.")
        if not await FusionService.get_by_id(db, fusion_id=input.fusion_id):
            raise ValueError(f"Fusion with ID {input.fusion_id} not found.")
            
        new_item = await CameraByFusionService.create(db, CameraByFusion(**input.__dict__))
        return CameraByFusionType(**new_item.dict())

    @strawberry.mutation
    async def update_camera_by_fusion(self, info: Info, fusion_id: int, camera_id: int, input: CameraByFusionUpdateInput) -> Optional[CameraByFusionType]:
        """Updates an existing CameraByFusion link by its composite ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await CameraByFusionService.update(db, fusion_id=fusion_id, camera_id=camera_id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"CameraByFusion with fID {fusion_id} and cID {camera_id} not found.")
        return CameraByFusionType(**updated_item.dict())

    @strawberry.mutation
    async def delete_camera_by_fusion(self, info: Info, fusion_id: int, camera_id: int) -> CameraByFusionType:
        """Deletes a CameraByFusion link by its composite ID."""
        db = info.context["db"]
        deleted_item = await CameraByFusionService.delete(db, fusion_id=fusion_id, camera_id=camera_id)
        if not deleted_item:
            raise ValueError(f"CameraByFusion with fID {fusion_id} and cID {camera_id} not found.")
        return CameraByFusionType(**deleted_item.dict())