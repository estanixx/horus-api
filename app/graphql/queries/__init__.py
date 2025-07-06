import strawberry
from .station_query import StationQuery
from .camera_query import CameraQuery
from .sensor_query import SensorQuery
from .image_query import ImageQuery

@strawberry.type
class Query(StationQuery, CameraQuery, SensorQuery, ImageQuery):
    """
    The root Query type for the GraphQL schema.

    This class combines all available queries by inheriting from the individual
    query classes. Strawberry automatically merges the fields from all parent classes into this single type,
    making them available at the root of the GraphQL query entry point.
    """
    pass