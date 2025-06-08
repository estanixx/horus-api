# app/graphql/types/camera_type.py
"""
Defines the GraphQL types related to the Camera entity.

This module contains the main `CameraType` for queries, as well as the
`CameraCreateInput` and `CameraUpdateInput` types used in mutations.
"""

import strawberry
from typing import Optional

# No need to import StationType here directly, as the CameraType doesn't
# have a nested 'station' field defined as a Strawberry field.
# If you wanted to include it, you would add `from app.graphql.types import StationType`
# and potentially handle circular dependencies on the Strawberry type level.


@strawberry.type
class CameraType:
    """
    Represents a camera in the GraphQL schema.

    This is the main object type that will be returned in queries and mutations
    for camera-related operations.

    Attributes:
        id: The unique identifier for the camera.
        reference: A user-defined reference or name for the camera.
        sizeX: The horizontal resolution (width) of the camera's sensor in pixels.
        sizeY: The vertical resolution (height) of the camera's sensor in pixels.
        station_id: The ID of the station this camera is associated with.
    """
    id: int
    reference: str
    sizeX: int
    sizeY: int
    # Foreign key can be exposed as a direct field in the GraphQL type.
    station_id: Optional[int] = None


@strawberry.input
class CameraCreateInput:
    """
    The input type for creating a new Camera.

    Used by the `createCamera` mutation. The `station_id` is required
    to ensure a camera is always linked to a station upon creation.
    """
    reference: str
    sizeX: int
    sizeY: int
    # A station must exist to link a new camera to it.
    station_id: int


@strawberry.input
class CameraUpdateInput:
    """
    The input type for updating an existing Camera.

    Used by the `updateCamera` mutation. All fields are optional, allowing
    for partial updates of a camera's attributes.
    """
    reference: Optional[str] = None
    sizeX: Optional[int] = None
    sizeY: Optional[int] = None
    # Allows for re-assigning the camera to a different station.
    station_id: Optional[int] = None