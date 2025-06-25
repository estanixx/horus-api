# app/graphql/mutations/station_mutation.py
"""
Defines the asynchronous GraphQL mutations for creating, updating, and deleting Station entities.

This module uses Strawberry to define the mutation fields and interacts with the
StationService to handle the business logic and asynchronous database operations.
"""

import strawberry
from typing import Optional

from app.graphql.types import StationType, StationCreateInput, StationUpdateInput
from app.models import Station
from app.services import StationService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class StationMutation:
    """Provides GraphQL mutations for the Station model."""

    @strawberry.mutation
    async def create_station(self, info, input: StationCreateInput) -> StationType:
        """
        Creates a new station record in the database.

        Args:
            info: The Strawberry resolver info object, used to access context like the DB session.
            input: A Strawberry input object containing the data for the new station.

        Returns:
            The newly created station, cast to the StationType for the GraphQL response.
        """
        # Extract the async database session from the GraphQL context.
        db: AsyncSession = info.context["db"]
        
        # Convert the Strawberry input object into a standard Python dictionary.
        input_dict = strawberry.asdict(input)
        
        # Create a SQLModel Station instance from the dictionary.
        # .parse_obj() is used for compatibility with older SQLModel/Pydantic versions.
        station_data = Station.parse_obj(input_dict)
        
        # Await the asynchronous service call to handle the creation and database commit.
        station = await StationService(db).create_station(station_data)
        

        return station # type: ignore

    @strawberry.mutation
    async def update_station(self, info, id: int, input: StationUpdateInput) -> Optional[StationType]:
        """
        Updates an existing station record by its ID using partial data.

        This mutation only changes the fields that are explicitly provided in the input.

        Args:
            info: The Strawberry resolver info object.
            id: The integer ID of the station to update.
            input: A Strawberry input object with the fields to update.

        Returns:
            The updated station object, or None if the station was not found.
        """
        db: AsyncSession = info.context["db"]
        
        # Convert the input to a dictionary, filtering out any keys that were not
        # provided in the mutation (i.e., their value is None).
        # This is crucial for performing partial updates correctly.
        input_dict = {k: v for k, v in strawberry.asdict(input).items() if v is not None}

        # Create a partial Station model instance with only the provided update data.
        station_data = Station.parse_obj(input_dict)

        # Await the asynchronous service call to find the station and apply the updates.
        station = await StationService(db).update_station(id, station_data)

        return station # type: ignore

    @strawberry.mutation
    async def delete_station(self, info, id: int) -> bool:
        """
        Deletes a station record from the database by its ID.

        Args:
            info: The Strawberry resolver info object.
            id: The integer ID of the station to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        db: AsyncSession = info.context["db"]
        
        # Await the asynchronous service call to delete the station.
        deleted = await StationService(db).delete_station(id)
        
        return deleted