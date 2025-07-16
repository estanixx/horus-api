from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .calibrationparameter_type import CalibrationParameterType

@strawberry.type
class CalibrationValueType:
    id_param: int
    id_col: int
    id_row: int
    value: float
    created_at: datetime
    updated_at: datetime

    parameter: Annotated["CalibrationParameterType", strawberry.lazy(".calibrationparameter_type")]

@strawberry.input
class CalibrationValueCreateInput:
    id_param: int
    id_col: int
    id_row: int
    value: float

@strawberry.input
class CalibrationValueUpdateInput:
    value: Optional[float] = None