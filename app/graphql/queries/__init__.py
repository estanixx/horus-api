# app/graphql/queries/__init__.py
"""
GraphQL Queries Barrel File.

This module aggregates all individual query classes from the 'queries'
directory into a single root 'Query' type. This approach keeps the
query logic organized in separate files while providing a single, unified
entry point for the Strawberry schema.
"""

import strawberry
from .station_query import StationQuery
from .camera_query import CameraQuery


@strawberry.type
class Query(StationQuery, CameraQuery):
    """
    The root Query type for the GraphQL schema.

    This class combines all available queries by inheriting from the individual
    query classes (e.g., `StationQuery`, `CameraQuery`). Strawberry
    automatically merges the fields from all parent classes into this single type,
    making them available at the root of the GraphQL query entry point.
    """
    pass