import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import CalibrationValueType, CalibrationValueCreateInput, CalibrationValueUpdateInput
from app.services import CalibrationValueService, CalibrationParameterService
from app.models import CalibrationValue

@strawberry.type
class CalibrationValueMutation:
    @strawberry.mutation
    async def create_calibration_value(self, info: Info, input: CalibrationValueCreateInput) -> CalibrationValueType:
        """Creates a new calibration value."""
        db = info.context["db"]
        if not await CalibrationParameterService.get_by_id(db, param_id=input.id_param):
            raise ValueError(f"CalibrationParameter with ID {input.id_param} not found.")
            
        new_item = await CalibrationValueService.create(db, CalibrationValue(**input.__dict__))
        return CalibrationValueType(**new_item.dict())

    @strawberry.mutation
    async def update_calibration_value(self, info: Info, id_param: int, id_col: int, id_row: int, input: CalibrationValueUpdateInput) -> Optional[CalibrationValueType]:
        """Updates an existing calibration value by its composite ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await CalibrationValueService.update(db, id_param=id_param, id_col=id_col, id_row=id_row, update_data=update_data)
        if not updated_item:
            raise ValueError(f"CalibrationValue with ID ({id_param}, {id_col}, {id_row}) not found.")
        return CalibrationValueType(**updated_item.dict())

    @strawberry.mutation
    async def delete_calibration_value(self, info: Info, id_param: int, id_col: int, id_row: int) -> CalibrationValueType:
        """Deletes a calibration value by its composite ID."""
        db = info.context["db"]
        deleted_item = await CalibrationValueService.delete(db, id_param=id_param, id_col=id_col, id_row=id_row)
        if not deleted_item:
            raise ValueError(f"CalibrationValue with ID ({id_param}, {id_col}, {id_row}) not found.")
        return CalibrationValueType(**deleted_item.dict())