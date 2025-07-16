import strawberry

from .station_queries import StationQuery
from .camera_queries import CameraQuery
from .sensor_queries import SensorQuery
from .gcp_queries import GCPQuery
from .automaticparams_queries import AutomaticParamsQuery
from .obliqueimage_queries import ObliqueImageQuery
from .rectifiedimage_queries import RectifiedImageQuery
from .timestack_queries import TimeStackQuery
from .imagetype_queries import ImageTypeQuery
from .mergedimage_queries import MergedImageQuery
from .fusion_queries import FusionQuery
from .camerabyfusion_queries import CameraByFusionQuery
from .fusionparameter_queries import FusionParameterQuery
from .fusionvalue_queries import FusionValueQuery
from .commonpoint_queries import CommonPointQuery
from .calibration_queries import CalibrationQuery
from .calibrationparameter_queries import CalibrationParameterQuery
from .calibrationvalue_queries import CalibrationValueQuery
from .pickedgcp_queries import PickedGCPQuery
from .roi_queries import ROIQuery
from .roicoordinate_queries import ROICoordinateQuery
from .measurement_queries import MeasurementQuery
from .measurementtype_queries import MeasurementTypeQuery
from .measurementvalue_queries import MeasurementValueQuery

@strawberry.type
class Query(
    StationQuery,
    CameraQuery,
    SensorQuery,
    GCPQuery,
    AutomaticParamsQuery,
    ObliqueImageQuery,
    RectifiedImageQuery,
    TimeStackQuery,
    ImageTypeQuery,
    MergedImageQuery,
    FusionQuery,
    CameraByFusionQuery,
    FusionParameterQuery,
    FusionValueQuery,
    CommonPointQuery,
    CalibrationQuery,
    CalibrationParameterQuery,
    CalibrationValueQuery,
    PickedGCPQuery,
    ROIQuery,
    ROICoordinateQuery,
    MeasurementQuery,
    MeasurementTypeQuery,
    MeasurementValueQuery,
):
    """Root query type for the GraphQL schema."""
    pass

__all__ = ["Query"]