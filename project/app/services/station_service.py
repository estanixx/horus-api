# app/services/station_service.py
"""
Service Layer for Station Operations.

This module provides the `StationService` class, which encapsulates the
business logic and data access operations for the Station model. This
separates the core application logic from the API layer (e.g., GraphQL resolvers).
"""

from typing import List, Optional
from sqlmodel import select
from app.models import Station
from sqlmodel.ext.asyncio.session import AsyncSession


class StationService:
    """
    Contains all business logic methods for interacting with the Station model.
    """
    def __init__(self, db: AsyncSession):
        """
        Initializes the service with a database session.

        Args:
            db: An `AsyncSession` object for database communication.
        """
        self.db = db

    async def get_all_stations(self) -> List[Station]:
        """
        Asynchronously retrieves all station records from the database.

        Returns:
            A list of all Station objects.
        """
        # Execute the select statement asynchronously.
        result = await self.db.exec(select(Station))
        # .all() gets all results from the executed statement.
        return result.all()

    async def get_station_by_id(self, station_id: int) -> Optional[Station]:
        """
        Asynchronously retrieves a single station by its primary key.

        Args:
            station_id: The integer ID of the station to retrieve.

        Returns:
            The Station object if found, otherwise None.
        """
        # .get() is an efficient way to look up an object by its primary key.
        return await self.db.get(Station, station_id)

    async def get_station_by_alias(self, alias: str) -> Optional[Station]:
        """
        Asynchronously retrieves a single station by its unique alias.

        Args:
            alias: The string alias of the station to retrieve.

        Returns:
            The Station object if a match is found, otherwise None.
        """
        statement = select(Station).where(Station.alias == alias)
        result = await self.db.exec(statement)
        # .first() gets the first result or None if there are no results.
        return result.first()

    async def create_station(self, station_create: Station) -> Station:
        """
        Asynchronously creates a new station record in the database.

        Args:
            station_create: A Station model instance with the data for the new record.

        Returns:
            The newly created and refreshed Station object, including its database-generated ID.
        """
        # Add the new station object to the session.
        self.db.add(station_create)
        # Commit the transaction to save the changes to the database.
        await self.db.commit()
        # Refresh the object to get the latest state from the database (e.g., the new ID).
        await self.db.refresh(station_create)
        return station_create

    async def update_station(self, station_id: int, station_update: Station) -> Optional[Station]:
        """
        Asynchronously updates an existing station record with partial data.

        Args:
            station_id: The ID of the station to update.
            station_update: A Station model instance containing the fields to update.

        Returns:
            The updated Station object, or None if the station was not found.
        """
        # First, retrieve the existing station from the database.
        station = await self.db.get(Station, station_id)
        if station:
            # CORRECTED: Use .dict() for compatibility with older SQLModel/Pydantic versions.
            # exclude_unset=True ensures we only get the fields that were actually provided.
            update_data = station_update.dict(exclude_unset=True)
            # Iterate over the provided update data and set the new values on the existing object.
            for key, value in update_data.items():
                setattr(station, key, value)
            
            # Add the updated object to the session and commit.
            self.db.add(station)
            await self.db.commit()
            await self.db.refresh(station)
        return station

    async def delete_station(self, station_id: int) -> bool:
        """
        Asynchronously deletes a station record by its primary key.

        Args:
            station_id: The ID of the station to delete.

        Returns:
            True if the station was deleted successfully, False otherwise.
        """
        station = await self.db.get(Station, station_id)
        if station:
            # Asynchronously delete the object from the database.
            await self.db.delete(station)
            await self.db.commit()
            return True
        return False