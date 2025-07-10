# app/graphql/mutations/sensor_mutations.py

"""
GraphQL mutation resolvers for the Sensor model.
"""

import strawberry
from strawberry.types import Info
from typing import Optional

from app.graphql.types import SensorType, SensorCreateInput, SensorUpdateInput
from app.services import SensorService, StationService

@strawberry.type
class SensorMutation:
    @strawberry.mutation
    async def create_sensor(self, info: Info, input: SensorCreateInput) -> SensorType:
        """Creates a new sensor and associates it with a station."""
        db = info.context["db"]
        # Ensure the station exists before creating a sensor for it
        if not await StationService.get_by_id(db, input.station_id):
             raise ValueError(f"Station with ID {input.station_id} not found.")

        new_sensor = await SensorService.create(db, data=input)
        return SensorType(**new_sensor.dict())

    @strawberry.mutation
    async def update_sensor(
        self, info: Info, id: int, input: SensorUpdateInput
    ) -> Optional[SensorType]:
        """Updates an existing sensor by its ID."""
        db = info.context["db"]
        updated_sensor = await SensorService.update(db, sensor_id=id, data=input)
        if not updated_sensor:
            raise ValueError(f"Sensor with ID {id} not found.")
        return SensorType(**updated_sensor.dict())

    @strawberry.mutation
    async def delete_sensor(self, info: Info, id: int) -> SensorType:
        """Deletes a sensor by its ID."""
        db = info.context["db"]
        deleted_sensor = await SensorService.delete(db, sensor_id=id)
        if not deleted_sensor:
            raise ValueError(f"Sensor with ID {id} not found.")
        return SensorType(**deleted_sensor.dict())