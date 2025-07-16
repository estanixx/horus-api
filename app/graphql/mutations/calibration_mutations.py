import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CalibrationType, CalibrationCreateInput, CalibrationUpdateInput
from app.services import CalibrationService, CameraService
from app.models import Calibration

@strawberry.type
class CalibrationMutation:
    @strawberry.mutation
    async def create_calibration(self, info: Info, input: CalibrationCreateInput) -> CalibrationType:
        """Creates a new calibration."""
        db = info.context["db"]
        if not await CameraService.get_by_id(db, camera_id=input.camera_id):
            raise ValueError(f"Camera with ID {input.camera_id} not found.")
            
        new_item = await CalibrationService.create(db, Calibration(**input.__dict__))
        return CalibrationType(**new_item.dict())

    @strawberry.mutation
    async def update_calibration(self, info: Info, id: int, input: CalibrationUpdateInput) -> Optional[CalibrationType]:
        """Updates an existing calibration by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await CalibrationService.update(db, calibration_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"Calibration with ID {id} not found.")
        return CalibrationType(**updated_item.dict())

    @strawberry.mutation
    async def delete_calibration(self, info: Info, id: int) -> CalibrationType:
        """Deletes a calibration by its ID."""
        db = info.context["db"]
        deleted_item = await CalibrationService.delete(db, calibration_id=id)
        if not deleted_item:
            raise ValueError(f"Calibration with ID {id} not found.")
        return CalibrationType(**deleted_item.dict())