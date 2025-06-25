from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .calibration import Calibration
    from .calibrationvalue import CalibrationValue


class CalibrationParameter(SQLModel, table=True):
    __tablename__ = "calibrationparameter"

    id: str = Field(
        sa_column=Column(
            "id",
            String,
            nullable=False,
            primary_key=True
        )
    )

    calibration_id: str = Field(
        sa_column=Column("calibration", String, nullable=False),
        foreign_key="calibration.idcalibration"
    )

    name: str

    calibration: Optional["Calibration"] = Relationship(back_populates="parameters")
    values: list["CalibrationValue"] = Relationship(back_populates="parameter")

