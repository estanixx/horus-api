from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, DECIMAL
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .calibration import Calibration
    from .roicoordinate import ROICoordinate


class ROI(SQLModel, table=True):
    __tablename__ = "roi"

    idroi: str = Field(
        sa_column=Column(
            "idroi",
            String,
            nullable=False,
            primary_key=True
        )
    )

    idcalibration: str = Field(
        sa_column=Column("idcalibration", String, nullable=False),
        foreign_key="calibration.idcalibration"
    )

    type: str
    timestamp: float = Field(
        sa_column=Column("timestamp", DECIMAL(17, 10), nullable=False)
    )

    calibration: Optional["Calibration"] = Relationship(back_populates="rois")
    coordinates: list["ROICoordinate"] = Relationship(back_populates="roi")

