from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey
from sqlalchemy import String, Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .calibration import Calibration
    from .calibrationvalue import CalibrationValue


class CalibrationParameter(BaseSQLModel, table=True):
    __tablename__ = "calibration_parameter"


    calibration_id: int = Field(
        sa_column=Column("calibration_id", Integer, ForeignKey("calibration.id"), nullable=False),
    )

    name: str

    calibration: Optional["Calibration"] = Relationship(back_populates="parameters")
    values: list["CalibrationValue"] = Relationship(back_populates="parameter")

