import strawberry

from .station_queries import StationQuery
from .camera_queries import CameraQuery
from .sensor_queries import SensorQuery
from .image_queries import ImageQuery
from .obliqueimage_queries import ObliqueImageQuery
from .rectifiedimage_queries import RectifiedImageQuery
from .mergeimage_queries import MergedImageQuery

@strawberry.type
class Query(StationQuery, CameraQuery, SensorQuery, ImageQuery, ObliqueImageQuery, RectifiedImageQuery, MergedImageQuery):
    """
    Root query type for the GraphQL schema.
    
    Inherits all query fields from the individual model query classes.
    """
    pass

__all__ = ["Query"]