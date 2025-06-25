import strawberry
from typing import Optional
from app.graphql.types import StationType, StationCreateInput, StationUpdateInput
from app.models import Station
from app.services import StationService
from sqlmodel.ext.asyncio.session import AsyncSession

@strawberry.type
class StationMutation:

    @strawberry.mutation
    async def create_station(self, info, input: StationCreateInput) -> StationType:
        db: AsyncSession = info.context["db"]
        input_dict = strawberry.asdict(input)
        station_data = Station.parse_obj(input_dict)
        station = await StationService(db).create_station(station_data)
        return station # type: ignore


    @strawberry.mutation
    async def update_station(self, info, id: int, input: StationUpdateInput) -> Optional[StationType]:
        db: AsyncSession = info.context["db"]
        input_dict = {k: v for k, v in strawberry.asdict(input).items() if v is not None}
        station_data = Station.parse_obj(input_dict)
        station = await StationService(db).update_station(id, station_data)
        return station # type: ignore


    @strawberry.mutation
    async def delete_station(self, info, id: int) -> bool:
        db: AsyncSession = info.context["db"]
        deleted = await StationService(db).delete_station(id)
        return deleted