# app/graphql/queries/__init__.py
import strawberry
from .station_query import StationQuery
from .camera_query import CameraQuery

# Combine all individual query types into a single root Query type
# This is a common pattern when breaking down large Query types
@strawberry.type
class Query(StationQuery, CameraQuery):
    pass