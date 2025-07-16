import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import PickedGCPType, PickedGCPCreateInput, PickedGCPUpdateInput
from app.services import PickedGCPService, CalibrationService, GCPService
from app.models import PickedGCP

@strawberry.type
class PickedGCPMutation:
    @strawberry.mutation
    async def create_picked_gcp(self, info: Info, input: PickedGCPCreateInput) -> PickedGCPType:
        """Creates a new PickedGCP link."""
        db = info.context["db"]
        if not await CalibrationService.get_by_id(db, calibration_id=input.calibration_id):
            raise ValueError(f"Calibration with ID {input.calibration_id} not found.")
        if not await GCPService.get_by_id(db, gcp_id=input.gcp_id):
            raise ValueError(f"GCP with ID {input.gcp_id} not found.")
            
        new_item = await PickedGCPService.create(db, PickedGCP(**input.__dict__))
        return PickedGCPType(**new_item.dict())

    @strawberry.mutation
    async def update_picked_gcp(self, info: Info, calibration_id: int, gcp_id: int, input: PickedGCPUpdateInput) -> Optional[PickedGCPType]:
        """Updates an existing PickedGCP link by its composite ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await PickedGCPService.update(db, calibration_id=calibration_id, gcp_id=gcp_id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"PickedGCP with cID {calibration_id} and gID {gcp_id} not found.")
        return PickedGCPType(**updated_item.dict())

    @strawberry.mutation
    async def delete_picked_gcp(self, info: Info, calibration_id: int, gcp_id: int) -> PickedGCPType:
        """Deletes a PickedGCP link by its composite ID."""
        db = info.context["db"]
        deleted_item = await PickedGCPService.delete(db, calibration_id=calibration_id, gcp_id=gcp_id)
        if not deleted_item:
            raise ValueError(f"PickedGCP with cID {calibration_id} and gID {gcp_id} not found.")
        return PickedGCPType(**deleted_item.dict())