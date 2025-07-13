import strawberry

from .station_mutations import StationMutation
from .camera_mutations import CameraMutation
from .sensor_mutations import SensorMutation
from .image_mutations import ImageMutation
from .obliqueimage_mutations import ObliqueImageMutation


@strawberry.type
class Mutation(StationMutation, CameraMutation, SensorMutation, ImageMutation, ObliqueImageMutation ):
    """
    The root Mutation type for the GraphQL schema.

    This class combines all available mutations by inheriting from the individual
    mutation classes. Strawberry
    automatically merges the fields from all parent classes into this single type,
    making them available at the root of the GraphQL mutation entry point.
    """
    pass