# app/graphql/types/station_type.py
import strawberry
from typing import List, Optional

# Relative import for CameraType within the same 'types' package
# if TYPE_CHECKING:
from app.graphql.types import CameraType

# Needed for the nested resolver
from app.services.camera_service import CameraService
from sqlmodel import Session # For type hinting

@strawberry.type
class StationType:
    id: int
    alias: str
    elevation: float
    lat: float
    lon: float
    country: str
    state: str
    city: str
    responsible: Optional[str] = None
    description: Optional[str] = None

    # List of cameras related to this station
    @strawberry.field
    def cameras(self, info) -> List['CameraType']:
        db: Session = info.context["db"]
        camera_service = CameraService(db)
        return camera_service.get_cameras_by_station_id(self.id)

@strawberry.input
class StationCreateInput:
    alias: str
    elevation: float
    lat: float
    lon: float
    country: str
    state: str
    city: str
    responsible: Optional[str] = None
    description: Optional[str] = None

@strawberry.input
class StationUpdateInput:
    alias: Optional[str] = None
    elevation: Optional[float] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    responsible: Optional[str] = None
    description: Optional[str] = None