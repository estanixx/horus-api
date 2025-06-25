# app/services/camera_service.py
"""
Service Layer for Camera Operations.

This module provides the `CameraService` class, which encapsulates the
business logic and data access operations for the Camera model. This
separates the core application logic from the API layer (e.g., GraphQL resolvers).
"""

from typing import List, Optional
from sqlmodel import select
from app.models import Camera
from sqlmodel.ext.asyncio.session import AsyncSession


class CameraService:
    """
    Contains all business logic methods for interacting with the Camera model.
    """
    def __init__(self, db: AsyncSession):
        """
        Initializes the service with a database session.

        Args:
            db: An `AsyncSession` object for database communication.
        """
        self.db = db

    async def get_all_cameras(self) -> List[Camera]:
        """
        Asynchronously retrieves all camera records from the database.

        Returns:
            A list of all Camera objects.
        """
        # Execute the select statement asynchronously.
        result = await self.db.exec(select(Camera))
        # .all() gets all results from the executed statement.
        return result.all()

    async def get_camera_by_id(self, camera_id: int) -> Optional[Camera]:
        """
        Asynchronously retrieves a single camera by its primary key.

        Args:
            camera_id: The integer ID of the camera to retrieve.

        Returns:
            The Camera object if found, otherwise None.
        """
        # .get() is an efficient way to look up an object by its primary key.
        return await self.db.get(Camera, camera_id)

    async def create_camera(self, camera_create: Camera) -> Camera:
        """
        Asynchronously creates a new camera record in the database.

        Args:
            camera_create: A Camera model instance with the data for the new record.

        Returns:
            The newly created and refreshed Camera object, including its database-generated ID.
        """
        # Add the new camera object to the session.
        self.db.add(camera_create)
        # Commit the transaction to save the changes to the database.
        await self.db.commit()
        # Refresh the object to get the latest state from the database (e.g., the new ID).
        await self.db.refresh(camera_create)
        return camera_create

    async def update_camera(self, camera_id: int, camera_update: Camera) -> Optional[Camera]:
        """
        Asynchronously updates an existing camera record with partial data.

        Args:
            camera_id: The ID of the camera to update.
            camera_update: A Camera model instance containing the fields to update.

        Returns:
            The updated Camera object, or None if the camera was not found.
        """
        # First, retrieve the existing camera from the database.
        camera = await self.db.get(Camera, camera_id)
        if camera:
            # CORRECTED: Use .dict() for compatibility with older SQLModel/Pydantic versions.
            # exclude_unset=True ensures we only get the fields that were actually provided.
            update_data = camera_update.dict(exclude_unset=True)
            # Iterate over the provided update data and set the new values on the existing object.
            for key, value in update_data.items():
                setattr(camera, key, value)
            
            # Add the updated object to the session and commit.
            self.db.add(camera)
            await self.db.commit()
            await self.db.refresh(camera)
        return camera

    async def delete_camera(self, camera_id: int) -> bool:
        """
        Asynchronously deletes a camera record by its primary key.

        Args:
            camera_id: The ID of the camera to delete.

        Returns:
            True if the camera was deleted successfully, False otherwise.
        """
        camera = await self.db.get(Camera, camera_id)
        if camera:
            # Asynchronously delete the object from the database.
            await self.db.delete(camera)
            await self.db.commit()
            return True
        return False
    
    async def get_cameras_by_station_id(self, station_id: int) -> List[Camera]:
        """
        Asynchronously retrieves all cameras associated with a specific station ID.

        Args:
            station_id: The ID of the station to find cameras for.

        Returns:
            A list of Camera objects belonging to the specified station.
        """
        # Build and execute a select statement with a 'where' clause.
        statement = select(Camera).where(Camera.station_id == station_id)
        result = await self.db.exec(statement)
        return result.all()