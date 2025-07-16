import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ROIType, ROICreateInput, ROIUpdateInput
from app.services import ROIService, CalibrationService
from app.models import ROI

@strawberry.type
class ROIMutation:
    @strawberry.mutation
    async def create_roi(self, info: Info, input: ROICreateInput) -> ROIType:
        """Creates a new Region of Interest (ROI)."""
        db = info.context["db"]
        if not await CalibrationService.get_by_id(db, calibration_id=input.calibration_id):
            raise ValueError(f"Calibration with ID {input.calibration_id} not found.")
            
        new_item = await ROIService.create(db, ROI(**input.__dict__))
        return ROIType(**new_item.dict())

    @strawberry.mutation
    async def update_roi(self, info: Info, id: int, input: ROIUpdateInput) -> Optional[ROIType]:
        """Updates an existing ROI by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await ROIService.update(db, roi_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"ROI with ID {id} not found.")
        return ROIType(**updated_item.dict())

    @strawberry.mutation
    async def delete_roi(self, info: Info, id: int) -> ROIType:
        """Deletes an ROI by its ID."""
        db = info.context["db"]
        deleted_item = await ROIService.delete(db, roi_id=id)
        if not deleted_item:
            raise ValueError(f"ROI with ID {id} not found.")
        return ROIType(**deleted_item.dict())