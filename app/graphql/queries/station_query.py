import strawberry
from typing import List, Optional
from app.graphql.types import StationType
from app.services import StationService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class StationQuery:
    """Provides GraphQL queries for the Station model."""

    @strawberry.field
    async def stations(self, info) -> List[StationType]:
        db: AsyncSession = info.context["db"]
        db_stations = await StationService(db).get_all_stations()

        return db_stations # type: ignore

    @strawberry.field
    async def station(self, info, id: int) -> Optional[StationType]:
        db: AsyncSession = info.context["db"]
        db_station = await StationService(db).get_station_by_id(id)

        if not db_station:
            return None

        return db_station # type: ignore