import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import StationType, StationCreateInput, StationUpdateInput
from app.services import StationService
from app.models import Station

@strawberry.type
class StationMutation:
    @strawberry.mutation
    async def create_station(self, info: Info, input: StationCreateInput) -> StationType:
        """Creates a new station."""
        db = info.context["db"]
        new_item = await StationService.create(db, Station(**input.__dict__))
        return StationType(**new_item.dict())

    @strawberry.mutation
    async def update_station(self, info: Info, id: int, input: StationUpdateInput) -> Optional[StationType]:
        """Updates an existing station by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await StationService.update(db, station_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"Station with ID {id} not found.")
        return StationType(**updated_item.dict())

    @strawberry.mutation
    async def delete_station(self, info: Info, id: int) -> StationType:
        """Deletes a station by its ID."""
        db = info.context["db"]
        deleted_item = await StationService.delete(db, station_id=id)
        if not deleted_item:
            raise ValueError(f"Station with ID {id} not found.")
        return StationType(**deleted_item.dict())