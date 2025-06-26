import strawberry
from typing import Optional
from app.graphql.types import SensorType, SensorCreateInput, SensorUpdateInput
from app.models import Sensor
from app.services import SensorService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class SensorMutation:

    @strawberry.mutation
    async def create_sensor(self, info, input: SensorCreateInput) -> SensorType:
        db: AsyncSession = info.context["db"]
        input_dict = strawberry.asdict(input)
        data = Sensor.parse_obj(input_dict)
        sensor = await SensorService(db).save_sensor(data)
        return sensor  # type: ignore

    @strawberry.mutation
    async def update_sensor(
        self, info, id: int, input: SensorUpdateInput
    ) -> Optional[SensorType]:
        db: AsyncSession = info.context["db"]
        input_dict = {
            k: v for k, v in strawberry.asdict(input).items() if v is not None
        }
        data = Sensor.parse_obj(input_dict)
        sensor = await SensorService(db).update_sensor(id, data)
        return sensor  # type: ignore

    @strawberry.mutation
    async def delete_sensor(self, info, id: int) -> bool:
        db: AsyncSession = info.context["db"]
        deleted = await SensorService(db).delete_sensor(id)
        return deleted
