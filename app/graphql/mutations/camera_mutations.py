# app/graphql/mutations/camera_mutations.py

"""
GraphQL mutation resolvers for the Camera model.
"""

import strawberry
from strawberry.types import Info
from typing import Optional

from app.graphql.types import CameraType, CameraCreateInput, CameraUpdateInput
from app.services import CameraService, StationService

@strawberry.type
class CameraMutation:
    @strawberry.mutation
    async def create_camera(self, info: Info, input: CameraCreateInput) -> CameraType:
        """Creates a new camera and associates it with a station."""
        db = info.context["db"]
        # Ensure the station exists before creating a camera for it
        if not await StationService.get_by_id(db, input.station_id):
             raise ValueError(f"Station with ID {input.station_id} not found.")
        
        new_camera = await CameraService.create(db, data=input)
        return CameraType(**new_camera.dict())

    @strawberry.mutation
    async def update_camera(
        self, info: Info, id: int, input: CameraUpdateInput
    ) -> Optional[CameraType]:
        """Updates an existing camera by its ID."""
        db = info.context["db"]
        updated_camera = await CameraService.update(db, camera_id=id, data=input)
        if not updated_camera:
            raise ValueError(f"Camera with ID {id} not found.")
        return CameraType(**updated_camera.dict())

    @strawberry.mutation
    async def delete_camera(self, info: Info, id: int) -> CameraType:
        """Deletes a camera by its ID."""
        db = info.context["db"]
        deleted_camera = await CameraService.delete(db, camera_id=id)
        if not deleted_camera:
            raise ValueError(f"Camera with ID {id} not found.")
        return CameraType(**deleted_camera.dict())