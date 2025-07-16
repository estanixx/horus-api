import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MeasurementType, MeasurementCreateInput, MeasurementUpdateInput
from app.services import MeasurementService, StationService, MeasurementTypeService
from app.models import Measurement

@strawberry.type
class MeasurementMutation:
    @strawberry.mutation
    async def create_measurement(self, info: Info, input: MeasurementCreateInput) -> MeasurementType:
        """Creates a new measurement."""
        db = info.context["db"]
        if not await StationService.get_by_id(db, station_id=input.station_id):
            raise ValueError(f"Station with ID {input.station_id} not found.")
        if not await MeasurementTypeService.get_by_id(db, type_id=input.measurement_type_id):
            raise ValueError(f"MeasurementType with ID {input.measurement_type_id} not found.")
            
        new_item = await MeasurementService.create(db, Measurement(**input.__dict__))
        return MeasurementType(**new_item.dict())

    @strawberry.mutation
    async def update_measurement(self, info: Info, id: int, input: MeasurementUpdateInput) -> Optional[MeasurementType]:
        """Updates an existing measurement by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await MeasurementService.update(db, measurement_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"Measurement with ID {id} not found.")
        return MeasurementType(**updated_item.dict())

    @strawberry.mutation
    async def delete_measurement(self, info: Info, id: int) -> MeasurementType:
        """Deletes a measurement by its ID."""
        db = info.context["db"]
        deleted_item = await MeasurementService.delete(db, measurement_id=id)
        if not deleted_item:
            raise ValueError(f"Measurement with ID {id} not found.")
        return MeasurementType(**deleted_item.dict())