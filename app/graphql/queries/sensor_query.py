import strawberry
from typing import List, Optional

from app.graphql.types import SensorType
from app.services.sensor_service import SensorService
from sqlmodel.ext.asyncio.session import AsyncSession

@strawberry.type
class SensorQuery:

    @strawberry.field
    async def sensors(self, info) -> List[SensorType]:
        db: AsyncSession = info.context["db"]
        db_sensors = await SensorService(db).get_all_sensors()
        return db_sensors # type: ignore


    @strawberry.field
    async def sensor(self, info, id: int) -> Optional[SensorType]:
        db: AsyncSession = info.context["db"]
        db_sensor = await SensorService(db).get_sensor_by_id(id)
        if not db_sensor:
            return None
        return db_sensor # type: ignore