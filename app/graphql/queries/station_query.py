# app/graphql/queries/station_query.py
"""
Defines the GraphQL queries for retrieving Station entities from the database.

This module uses Strawberry to define the query fields and interacts with the
StationService to handle the business logic and asynchronous database operations.
"""

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
        """
        Retrieves a list of all stations from the database.

        Args:
            info: The Strawberry resolver info object, used to access context like the DB session.

        Returns:
            A list of all station objects, with each object cast to the StationType.
        """
        # Extract the async database session from the GraphQL context.
        db: AsyncSession = info.context["db"]

        # Await the asynchronous service call to fetch all stations.
        db_stations = await StationService(db).get_all_stations()

        return db_stations # type: ignore

    @strawberry.field
    async def station(self, info, id: int) -> Optional[StationType]:
        """
        Retrieves a single station by its unique ID.

        Args:
            info: The Strawberry resolver info object.
            id: The integer ID of the station to retrieve.

        Returns:
            The station object if found, otherwise None. The result is cast to StationType.
        """
        db: AsyncSession = info.context["db"]

        # Await the asynchronous service call to fetch a single station by its ID.
        db_station = await StationService(db).get_station_by_id(id)

        # If the service returns None (not found), the GraphQL response will be null.
        if not db_station:
            return None

        return db_station # type: ignore