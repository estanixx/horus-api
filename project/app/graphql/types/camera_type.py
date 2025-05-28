# app/graphql/types/camera_type.py
import strawberry
from typing import Optional

# No need to import StationType here directly, as the CameraType doesn't
# have a nested 'station' field defined as a Strawberry field.
# If you wanted to include it, you would add `from app.graphql.types import StationType`
# and potentially handle circular dependencies on the Strawberry type level.

@strawberry.type
class CameraType:
    id: int
    reference: str
    sizeX: int
    sizeY: int
    station_id: Optional[int] # Foreign key can be exposed
    
@strawberry.input
class CameraCreateInput:
    reference: str
    sizeX: int
    sizeY: int
    station_id: int # Station must exist to link a camera

@strawberry.input
class CameraUpdateInput:
    reference: Optional[str] = None
    sizeX: Optional[int] = None
    sizeY: Optional[int] = None
    station_id: Optional[int] = None # Can re-assign station