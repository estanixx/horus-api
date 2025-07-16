import strawberry

from .station_mutations import StationMutation
from .camera_mutations import CameraMutation
from .sensor_mutations import SensorMutation
from .gcp_mutations import GCPMutation
from .automaticparams_mutations import AutomaticParamsMutation
from .obliqueimage_mutations import ObliqueImageMutation
from .rectifiedimage_mutations import RectifiedImageMutation
from .timestack_mutations import TimeStackMutation
from .imagetype_mutations import ImageTypeMutation
from .mergedimage_mutations import MergedImageMutation
from .fusion_mutations import FusionMutation
from .camerabyfusion_mutations import CameraByFusionMutation
from .fusionparameter_mutations import FusionParameterMutation
from .fusionvalue_mutations import FusionValueMutation
from .commonpoint_mutations import CommonPointMutation
from .calibration_mutations import CalibrationMutation
from .calibrationparameter_mutations import CalibrationParameterMutation
from .calibrationvalue_mutations import CalibrationValueMutation
from .pickedgcp_mutations import PickedGCPMutation
from .roi_mutations import ROIMutation
from .roicoordinate_mutations import ROICoordinateMutation
from .measurement_mutations import MeasurementMutation
from .measurementtype_mutations import MeasurementTypeMutation
from .measurementvalue_mutations import MeasurementValueMutation

@strawberry.type
class Mutation(
    StationMutation,
    CameraMutation,
    SensorMutation,
    GCPMutation,
    AutomaticParamsMutation,
    ObliqueImageMutation,
    RectifiedImageMutation,
    TimeStackMutation,
    ImageTypeMutation,
    MergedImageMutation,
    FusionMutation,
    CameraByFusionMutation,
    FusionParameterMutation,
    FusionValueMutation,
    CommonPointMutation,
    CalibrationMutation,
    CalibrationParameterMutation,
    CalibrationValueMutation,
    PickedGCPMutation,
    ROIMutation,
    ROICoordinateMutation,
    MeasurementMutation,
    MeasurementTypeMutation,
    MeasurementValueMutation,
):
    """The root Mutation type for the GraphQL schema."""
    pass

__all__ = ["Mutation"]