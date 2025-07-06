from sqlmodel import Field, Relationship, Column
from sqlalchemy import Integer, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import TimestampsSQLModel

if TYPE_CHECKING:
    from .calibrationparameter import CalibrationParameter

class CalibrationValue(TimestampsSQLModel, table=True):
    __tablename__ = "calibration_value"

    id_param: int = Field(
        sa_column=Column(
            "id_param",
            Integer,
            ForeignKey("calibration_parameter.id"),
            nullable=False,
            primary_key=True 
        )
    )
    id_col: int = Field(
        sa_column=Column("id_col", Integer, nullable=False, primary_key=True),
    )
    id_row: int = Field(
        sa_column=Column("id_row", Integer, nullable=False, primary_key=True),
    )
    value: float = Field(
        sa_column=Column("value", Float, nullable=False)
    )

    parameter: Optional["CalibrationParameter"] = Relationship(back_populates="values")
