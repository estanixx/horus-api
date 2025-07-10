# app/graphql/mutations/station_mutations.py

"""
GraphQL mutation resolvers for the Station model.
"""
import strawberry
from strawberry.types import Info
from typing import Optional

from app.graphql.types import StationType, StationCreateInput, StationUpdateInput
from app.services import StationService

@strawberry.type
class StationMutation:
    @strawberry.mutation
    async def create_station(self, info: Info, input: StationCreateInput) -> StationType:
        """Creates a new station."""
        db = info.context["db"]
        new_station = await StationService.create(db, data=input)
        # Use .dict() for SQLModel objects for compatibility
        return StationType(**new_station.dict())

    @strawberry.mutation
    async def update_station(
        self, info: Info, id: int, input: StationUpdateInput
    ) -> Optional[StationType]:
        """Updates an existing station by its ID."""
        db = info.context["db"]
        updated_station = await StationService.update(db, station_id=id, data=input)
        if not updated_station:
            raise ValueError(f"Station with ID {id} not found.")
        # Use .dict() for SQLModel objects for compatibility
        return StationType(**updated_station.dict())

    @strawberry.mutation
    async def delete_station(self, info: Info, id: int) -> StationType:
        """Deletes a station by its ID."""
        db = info.context["db"]
        deleted_station = await StationService.delete(db, station_id=id)
        if not deleted_station:
            raise ValueError(f"Station with ID {id} not found.")
        # Use .dict() for SQLModel objects for compatibility
        return StationType(**deleted_station.dict())