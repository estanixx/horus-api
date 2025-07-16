import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MeasurementValueType, MeasurementValueCreateInput, MeasurementValueUpdateInput
from app.services import MeasurementValueService, MeasurementService
from app.models import MeasurementValue

@strawberry.type
class MeasurementValueMutation:
    @strawberry.mutation
    async def create_measurement_value(self, info: Info, input: MeasurementValueCreateInput) -> MeasurementValueType:
        """Creates a new measurement value."""
        db = info.context["db"]
        if not await MeasurementService.get_by_id(db, measurement_id=input.measurement_id):
            raise ValueError(f"Measurement with ID {input.measurement_id} not found.")
            
        new_item = await MeasurementValueService.create(db, MeasurementValue(**input.__dict__))
        return MeasurementValueType(**new_item.dict())

    @strawberry.mutation
    async def update_measurement_value(self, info: Info, measurement_id: int, id_col: int, id_row: int, id_depth: int, input: MeasurementValueUpdateInput) -> Optional[MeasurementValueType]:
        """Updates an existing measurement value by its composite ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await MeasurementValueService.update(db, measurement_id=measurement_id, id_col=id_col, id_row=id_row, id_depth=id_depth, update_data=update_data)
        if not updated_item:
            raise ValueError(f"MeasurementValue with ID ({measurement_id}, {id_col}, {id_row}, {id_depth}) not found.")
        return MeasurementValueType(**updated_item.dict())

    @strawberry.mutation
    async def delete_measurement_value(self, info: Info, measurement_id: int, id_col: int, id_row: int, id_depth: int) -> MeasurementValueType:
        """Deletes a measurement value by its composite ID."""
        db = info.context["db"]
        deleted_item = await MeasurementValueService.delete(db, measurement_id=measurement_id, id_col=id_col, id_row=id_row, id_depth=id_depth)
        if not deleted_item:
            raise ValueError(f"MeasurementValue with ID ({measurement_id}, {id_col}, {id_row}, {id_depth}) not found.")
        return MeasurementValueType(**deleted_item.dict())