# app/graphql/mutations/camera_mutation.py
"""
Defines the GraphQL mutations for creating, updating, and deleting Camera entities.

This module uses Strawberry to define the mutation fields and interacts with the
CameraService to handle the business logic and database operations.
"""

import strawberry
from typing import Optional

from app.graphql.types import CameraType, CameraCreateInput, CameraUpdateInput
from app.models import Camera
from app.services import CameraService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class CameraMutation:
    """Provides GraphQL mutations for the Camera model."""

    @strawberry.mutation
    async def create_camera(self, info, input: CameraCreateInput) -> CameraType:
        """
        Creates a new camera record in the database.

        Args:
            info: The Strawberry resolver info object, used to access context like the DB session.
            input: A Strawberry input object containing the data for the new camera.

        Returns:
            The newly created camera, cast to the CameraType for the GraphQL response.
        """
        # Extract the async database session from the GraphQL context.
        db: AsyncSession = info.context["db"]
        
        # Convert the Strawberry input object into a standard Python dictionary.
        input_dict = strawberry.asdict(input)
        
        # Create a SQLModel Camera instance from the dictionary.
        # .parse_obj() is used for compatibility with older SQLModel/Pydantic versions.
        camera_data = Camera.parse_obj(input_dict)

        # Call the service layer to handle the creation logic and database commit.
        camera = await CameraService(db).create_camera(camera_data)


        return camera # type: ignore

    @strawberry.mutation
    async def update_camera(self, info, id: int, input: CameraUpdateInput) -> Optional[CameraType]:
        """
        Updates an existing camera record by its ID.

        This mutation performs a partial update, only changing the fields
        that are provided in the input.

        Args:
            info: The Strawberry resolver info object.
            id: The integer ID of the camera to update.
            input: A Strawberry input object with the fields to update.

        Returns:
            The updated camera object, or None if the camera was not found.
        """
        db: AsyncSession = info.context["db"]
        
        # Convert the input to a dictionary, filtering out any keys that were not
        # provided in the mutation (i.e., their value is None).
        # This is crucial for performing partial updates correctly.
        input_dict = {k: v for k, v in strawberry.asdict(input).items() if v is not None}
        
        # Create a partial Camera model instance with only the provided update data.
        camera_data = Camera.parse_obj(input_dict)

        # Call the service layer to find the camera and apply the updates.
        camera = await CameraService(db).update_camera(id, camera_data)

        return camera  # type: ignore

    @strawberry.mutation
    async def delete_camera(self, info, id: int) -> bool:
        """
        Deletes a camera record from the database by its ID.

        Args:
            info: The Strawberry resolver info object.
            id: The integer ID of the camera to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        db: AsyncSession = info.context["db"]
        deleted = await CameraService(db).delete_camera(id)
        return deleted