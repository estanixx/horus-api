# app/graphql/types/station_type.py
"""
Defines the GraphQL types related to the Station entity.

This module contains the main `StationType` for queries, which includes a
resolver for fetching related cameras, as well as the `StationCreateInput`
and `StationUpdateInput` types used in mutations.
"""

import strawberry
from typing import List, Optional

# The 'if TYPE_CHECKING:' block prevents circular import errors at runtime
# while still allowing type checkers to see the import.
from .camera_type import CameraType

from app.services.camera_service import CameraService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class StationType:
    """
    Represents a weather station in the GraphQL schema.

    This is the main object type returned by station-related queries and mutations.
    It includes a resolver to fetch its associated cameras.

    Attributes:
        id: The unique identifier for the station.
        alias: A user-defined alias or name for the station.
        elevation: The station's elevation above sea level.
        lat: The latitude of the station's location.
        lon: The longitude of the station's location.
        country: The country where the station is located.
        state: The state or province where the station is located.
        city: The city where the station is located.
        responsible: The name or entity responsible for the station.
        description: A free-text description of the station.
    """
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

    @strawberry.field
    async def cameras(self, info) -> List['CameraType']:
        """Resolver to fetch the list of cameras associated with this station."""
        db: AsyncSession = info.context["db"]
        # The 'self' object here is the parent StationType instance.
        # We use its ID to fetch the related cameras.
        db_cameras = await CameraService(db).get_cameras_by_station_id(self.id)
        return db_cameras # type: ignore


@strawberry.input
class StationCreateInput:
    """The input type for creating a new Station."""
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
    """
    The input type for updating an existing Station.

    All fields are optional to allow for partial updates.
    """
    alias: Optional[str] = None
    elevation: Optional[float] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    responsible: Optional[str] = None
    description: Optional[str] = None