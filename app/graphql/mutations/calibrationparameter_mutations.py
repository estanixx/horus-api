import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CalibrationParameterType, CalibrationParameterCreateInput, CalibrationParameterUpdateInput
from app.services import CalibrationParameterService, CalibrationService
from app.models import CalibrationParameter

@strawberry.type
class CalibrationParameterMutation:
    @strawberry.mutation
    async def create_calibration_parameter(self, info: Info, input: CalibrationParameterCreateInput) -> CalibrationParameterType:
        """Creates a new calibration parameter."""
        db = info.context["db"]
        if not await CalibrationService.get_by_id(db, calibration_id=input.calibration_id):
            raise ValueError(f"Calibration with ID {input.calibration_id} not found.")
            
        new_item = await CalibrationParameterService.create(db, CalibrationParameter(**input.__dict__))
        return CalibrationParameterType(**new_item.dict())

    @strawberry.mutation
    async def update_calibration_parameter(self, info: Info, id: int, input: CalibrationParameterUpdateInput) -> Optional[CalibrationParameterType]:
        """Updates an existing calibration parameter by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await CalibrationParameterService.update(db, param_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"CalibrationParameter with ID {id} not found.")
        return CalibrationParameterType(**updated_item.dict())

    @strawberry.mutation
    async def delete_calibration_parameter(self, info: Info, id: int) -> CalibrationParameterType:
        """Deletes a calibration parameter by its ID."""
        db = info.context["db"]
        deleted_item = await CalibrationParameterService.delete(db, param_id=id)
        if not deleted_item:
            raise ValueError(f"CalibrationParameter with ID {id} not found.")
        return CalibrationParameterType(**deleted_item.dict())