import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MeasurementTypeType, MeasurementTypeCreateInput, MeasurementTypeUpdateInput
from app.services import MeasurementTypeService, SensorService
from app.models import MeasurementType

@strawberry.type
class MeasurementTypeMutation:
    @strawberry.mutation
    async def create_measurement_type(self, info: Info, input: MeasurementTypeCreateInput) -> MeasurementTypeType:
        """Creates a new measurement type."""
        db = info.context["db"]
        if not await SensorService.get_by_id(db, sensor_id=input.sensor_id):
            raise ValueError(f"Sensor with ID {input.sensor_id} not found.")
            
        new_item = await MeasurementTypeService.create(db, MeasurementType(**input.__dict__))
        return MeasurementTypeType(**new_item.dict())

    @strawberry.mutation
    async def update_measurement_type(self, info: Info, id: int, input: MeasurementTypeUpdateInput) -> Optional[MeasurementTypeType]:
        """Updates an existing measurement type by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await MeasurementTypeService.update(db, type_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"MeasurementType with ID {id} not found.")
        return MeasurementTypeType(**updated_item.dict())

    @strawberry.mutation
    async def delete_measurement_type(self, info: Info, id: int) -> MeasurementTypeType:
        """Deletes a measurement type by its ID."""
        db = info.context["db"]
        deleted_item = await MeasurementTypeService.delete(db, type_id=id)
        if not deleted_item:
            raise ValueError(f"MeasurementType with ID {id} not found.")
        return MeasurementTypeType(**deleted_item.dict())