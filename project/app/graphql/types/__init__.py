from .camera_type import CameraType, CameraCreateInput, CameraUpdateInput
from .station_type import StationType, StationCreateInput, StationUpdateInput

# Optionally define __all__ if you use from app.graphql.types import *
__all__ = [
    "StationType", "StationCreateInput", "StationUpdateInput",
    "CameraType", "CameraCreateInput", "CameraUpdateInput",
]