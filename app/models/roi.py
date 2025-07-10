from sqlmodel import SQLModel, Field, Relationship, Column, Integer, ForeignKey
from sqlalchemy import String, DECIMAL
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel
if TYPE_CHECKING:
    from .calibration import Calibration
    from .roicoordinate import ROICoordinate


class ROI(BaseSQLModel, table=True):
    __tablename__ = "roi"

    calibration_id: int = Field(
        sa_column=Column("calibration_id", Integer, ForeignKey("calibration.id"), nullable=False),
        
    )

    type: str
    timestamp: float = Field(
        sa_column=Column("timestamp", DECIMAL(17, 10), nullable=False)
    )

    calibration: Optional["Calibration"] = Relationship(back_populates="rois")
    coordinates: list["ROICoordinate"] = Relationship(back_populates="roi")

