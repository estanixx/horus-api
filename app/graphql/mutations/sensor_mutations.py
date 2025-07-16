import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import SensorType, SensorCreateInput, SensorUpdateInput
from app.services import SensorService, StationService
from app.models import Sensor

@strawberry.type
class SensorMutation:
    @strawberry.mutation
    async def create_sensor(self, info: Info, input: SensorCreateInput) -> SensorType:
        """Creates a new sensor and associates it with a station."""
        db = info.context["db"]
        if not await StationService.get_by_id(db, station_id=input.station_id):
            raise ValueError(f"Station with ID {input.station_id} not found.")
            
        new_item = await SensorService.create(db, Sensor(**input.__dict__))
        return SensorType(**new_item.dict())

    @strawberry.mutation
    async def update_sensor(self, info: Info, id: int, input: SensorUpdateInput) -> Optional[SensorType]:
        """Updates an existing sensor by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await SensorService.update(db, sensor_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"Sensor with ID {id} not found.")
        return SensorType(**updated_item.dict())

    @strawberry.mutation
    async def delete_sensor(self, info: Info, id: int) -> SensorType:
        """Deletes a sensor by its ID."""
        db = info.context["db"]
        deleted_item = await SensorService.delete(db, sensor_id=id)
        if not deleted_item:
            raise ValueError(f"Sensor with ID {id} not found.")
        return SensorType(**deleted_item.dict())