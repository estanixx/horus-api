# app/graphql/queries/camera_query.py
import strawberry
from typing import List, Optional
from app.graphql.types import CameraType # Import from the types barrel
from app.services.camera_service import CameraService
from sqlmodel import Session # For type hinting the db session

@strawberry.type
class CameraQuery:
    @strawberry.field
    def cameras(self, info) -> List[CameraType]:
        db: Session = info.context["db"]
        return CameraService(db).get_all_cameras()

    @strawberry.field
    def camera(self, info, id: int) -> Optional[CameraType]:
        db: Session = info.context["db"]
        return CameraService(db).get_camera_by_id(id)