from datetime import datetime
import strawberry
from typing import Optional, Annotated, TYPE_CHECKING

if TYPE_CHECKING:
    from .fusionparameter_type import FusionParameterType

@strawberry.type
class FusionValueType:
    matrix_id: int
    id_col: int
    id_row: int
    value: float
    created_at: datetime
    updated_at: datetime

    parameter: Annotated["FusionParameterType", strawberry.lazy(".fusionparameter_type")]

@strawberry.input
class FusionValueCreateInput:
    matrix_id: int
    id_col: int
    id_row: int
    value: float

@strawberry.input
class FusionValueUpdateInput:
    value: Optional[float] = None