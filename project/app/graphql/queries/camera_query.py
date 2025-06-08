# app/graphql/queries/camera_query.py
"""
Defines the GraphQL queries for retrieving Camera entities from the database.

This module uses Strawberry to define the query fields and interacts with the
CameraService to handle the business logic and asynchronous database operations.
"""

import strawberry
from typing import List, Optional

from app.graphql.types import CameraType
from app.services.camera_service import CameraService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class CameraQuery:
    """Provides GraphQL queries for the Camera model."""

    @strawberry.field
    async def cameras(self, info) -> List[CameraType]:
        """
        Retrieves a list of all cameras from the database.

        Args:
            info: The Strawberry resolver info object, used to access context like the DB session.

        Returns:
            A list of all camera objects, with each object cast to the CameraType.
        """
        # Extract the async database session from the GraphQL context.
        db: AsyncSession = info.context["db"]

        # Await the asynchronous service call to fetch all cameras.
        db_cameras = await CameraService(db).get_all_cameras()

        return db_cameras # type: ignore

    @strawberry.field
    async def camera(self, info, id: int) -> Optional[CameraType]:
        """
        Retrieves a single camera by its unique ID.

        Args:
            info: The Strawberry resolver info object.
            id: The integer ID of the camera to retrieve.

        Returns:
            The camera object if found, otherwise None. The result is cast to CameraType.
        """
        db: AsyncSession = info.context["db"]

        # Await the asynchronous service call to fetch a single camera by its ID.
        db_camera = await CameraService(db).get_camera_by_id(id)

        # If the service returns None (not found), the GraphQL response will be null.
        if not db_camera:
            return None

        return db_camera # type: ignore