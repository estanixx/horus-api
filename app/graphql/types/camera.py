from datetime import datetime
import strawberry
from typing import Optional, Annotated
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .station import StationType

@strawberry.type
class CameraType:
    """GraphQL type for the Camera model."""
    id: strawberry.ID
    created_at: datetime
    updated_at: datetime
    reference: str
    sizeX: int
    sizeY: int
    station_id: int
    station: Annotated["StationType", strawberry.lazy(".station")]

@strawberry.input
class CameraCreateInput:
    """GraphQL input type for creating a new Camera."""
    reference: str
    sizeX: int
    sizeY: int
    station_id: int

@strawberry.input
class CameraUpdateInput:
    """GraphQL input type for updating an existing Camera."""
    reference: Optional[str] = None
    sizeX: Optional[int] = None
    sizeY: Optional[int] = None