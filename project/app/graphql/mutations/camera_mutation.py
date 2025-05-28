# app/graphql/mutations/camera_mutation.py
import strawberry
from typing import Optional
from app.graphql.types import CameraType, CameraCreateInput, CameraUpdateInput # From types barrel
from app.models import Camera # Import SQLModel for conversion
from app.services.camera_service import CameraService
from sqlmodel import Session # For type hinting the db session

@strawberry.type
class CameraMutation:
    @strawberry.mutation
    def create_camera(self, info, input: CameraCreateInput) -> CameraType:
        db: Session = info.context["db"]
        camera_data = Camera.model_validate(input.model_dump())
        return CameraService(db).create_camera(camera_data)

    @strawberry.mutation
    def update_camera(self, info, id: int, input: CameraUpdateInput) -> Optional[CameraType]:
        db: Session = info.context["db"]
        camera_data = Camera.model_validate(input.model_dump(exclude_unset=True))
        return CameraService(db).update_camera(id, camera_data)

    @strawberry.mutation
    def delete_camera(self, info, id: int) -> bool:
        db: Session = info.context["db"]
        return CameraService(db).delete_camera(id)