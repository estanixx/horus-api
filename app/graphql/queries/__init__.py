# app/graphql/queries/__init__.py

"""
Barrel file for exporting and combining all GraphQL query resolvers.

This module imports all the individual query classes (e.g., StationQuery,
CameraQuery) and composes them into a single root `Query` type. This
pattern allows for a modular and organized schema definition.
"""

import strawberry

from .station_queries import StationQuery
from .camera_queries import CameraQuery
from .sensor_queries import SensorQuery

@strawberry.type
class Query(StationQuery, CameraQuery, SensorQuery):
    """
    Root query type for the GraphQL schema.
    
    Inherits all query fields from the individual model query classes.
    """
    pass

__all__ = ["Query"]