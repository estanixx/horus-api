from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .measurement_type import MeasurementType

@strawberry.type
class MeasurementValueType:
    measurement_id: int
    id_col: int
    id_row: int
    id_depth: int
    value: float
    created_at: datetime
    updated_at: datetime

    measurement: Annotated["MeasurementType", strawberry.lazy(".measurement_type")]

@strawberry.input
class MeasurementValueCreateInput:
    measurement_id: int
    id_col: int
    id_row: int
    id_depth: int
    value: float

@strawberry.input
class MeasurementValueUpdateInput:
    value: Optional[float] = None