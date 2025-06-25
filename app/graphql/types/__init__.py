"""
GraphQL Types Barrel File.

This module serves as a single entry point for all GraphQL types defined
within this directory. It imports types from their respective files
(e.g., `station_type.py`, `camera_type.py`) and exposes them from this
central location.

This allows for cleaner imports in other parts of the application, such as:
`from app.graphql.types import StationType, CameraCreateInput`
"""

# Import all GraphQL types to make them accessible from this module.
from .camera_type import CameraType, CameraCreateInput, CameraUpdateInput
from .station_type import StationType, StationCreateInput, StationUpdateInput

# Define the public API for this module when using wildcard imports (from . import *).
# This explicitly lists which names are part of the public interface.
__all__ = [
    "StationType", "StationCreateInput", "StationUpdateInput",
    "CameraType", "CameraCreateInput", "CameraUpdateInput",
]