
# app/graphql/types/__init__.py

"""
Barrel file for exporting all GraphQL types.

This file makes it convenient to import any type from the `app.graphql.types`
module, simplifying imports in resolvers and the schema definition.
"""

from .common import PageInfo, Edge, Connection
from .station import StationType, StationCreateInput, StationUpdateInput
from .camera import CameraType, CameraCreateInput, CameraUpdateInput
from .sensor import SensorType, SensorCreateInput, SensorUpdateInput
from .image import ImageType, ImageCreateInput, ImageUpdateInput


__all__ = [
    "PageInfo",
    "Edge",
    "Connection",
    "StationType",
    "StationCreateInput",
    "StationUpdateInput",
    "CameraType",
    "CameraCreateInput",
    "CameraUpdateInput",
    "SensorType",
    "SensorCreateInput",
    "SensorUpdateInput",
    "ImageType",
    "ImageCreateInput",
    "ImageUpdateInput"
]