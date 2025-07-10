# app/graphql/types/station.py

"""
GraphQL types for the Station model.

This module defines the main `StationType` for representing station data in
the GraphQL schema. It also includes `Strawberry.input` types for creating
and updating stations, which are used in mutations.
"""
from datetime import datetime
import strawberry
from typing import List, Optional, Annotated, TYPE_CHECKING
from strawberry.types import Info
from app.services import CameraService, SensorService
if TYPE_CHECKING:
    from .camera import CameraType
    from .sensor import SensorType
    
@strawberry.type
class StationType:
    """GraphQL type for the Station model."""
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    alias: str
    elevation: float
    lat: float
    lon: float
    country: str
    state: str
    city: str
    responsible: Optional[str]
    description: Optional[str]

    @strawberry.field
    async def cameras(
        self, info: Info, skip: int = 0, limit: int = 20
    ) -> List[Annotated["CameraType", strawberry.lazy(".camera")]]:
        """
        Fetches a list of cameras associated with this station.
        This resolver is executed only when the 'cameras' field is in a query.
        """
        # 'self' is the parent Station object
        db = info.context["db"]
        # The service returns a tuple of (items, total_count), we only need the items.
        cameras, _ = await CameraService.get_for_station(
            db=db, station_id=self.id, skip=skip, limit=limit
        )
        return cameras

    @strawberry.field
    async def sensors(
        self, info: Info, skip: int = 0, limit: int = 20
    ) -> List[Annotated["SensorType", strawberry.lazy(".sensor")]]:
        """
        Fetches a list of sensors associated with this station.
        This resolver is executed only when the 'sensors' field is in a query.
        """
        # 'self' is the parent Station object
        db = info.context["db"]
        sensors, _ = await SensorService.get_for_station(
            db=db, station_id=self.id, skip=skip, limit=limit
        )
        return sensors

@strawberry.input
class StationCreateInput:
    """GraphQL input type for creating a new Station."""
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
    """GraphQL input type for updating an existing Station."""
    alias: Optional[str] = None
    elevation: Optional[float] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    responsible: Optional[str] = None
    description: Optional[str] = None