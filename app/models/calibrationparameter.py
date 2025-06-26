from sqlmodel import SQLModel, Field, Relationship, Column
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
        sa_column=Column("calibration", Integer, nullable=False),
        foreign_key="calibration.id"
    )

    name: str

    calibration: Optional["Calibration"] = Relationship(back_populates="parameters")
    values: list["CalibrationValue"] = Relationship(back_populates="parameter")

