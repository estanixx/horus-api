# app/graphql/mutations/__init__.py
"""
GraphQL Mutations Barrel File.

This module aggregates all the individual mutation classes from the 'mutations'
directory into a single root 'Mutation' type. This approach keeps the
mutation logic organized in separate files while providing a single, unified
entry point for the Strawberry schema.
"""

import strawberry
from .station_mutation import StationMutation
from .camera_mutation import CameraMutation


@strawberry.type
class Mutation(StationMutation, CameraMutation):
    """
    The root Mutation type for the GraphQL schema.

    This class combines all available mutations by inheriting from the individual
    mutation classes (e.g., `StationMutation`, `CameraMutation`). Strawberry
    automatically merges the fields from all parent classes into this single type,
    making them available at the root of the GraphQL mutation entry point.
    """
    pass