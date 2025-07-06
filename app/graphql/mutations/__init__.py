import strawberry
from .station_mutation import StationMutation
from .camera_mutation import CameraMutation
from .sensor_mutation import SensorMutation
from .image_mutation import ImageMutation


@strawberry.type
class Mutation(StationMutation, CameraMutation, SensorMutation, ImageMutation ):
    """
    The root Mutation type for the GraphQL schema.

    This class combines all available mutations by inheriting from the individual
    mutation classes. Strawberry
    automatically merges the fields from all parent classes into this single type,
    making them available at the root of the GraphQL mutation entry point.
    """
    pass