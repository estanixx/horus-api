from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, DECIMAL, Integer, ForeignKey
from typing import Optional, List
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .camera import Camera
    from .rectifiedimage import RectifiedImage
    from .pickedgcp import PickedGCP
    from .calibrationparameter import CalibrationParameter
    from .roi import ROI
    

class Calibration(BaseSQLModel, table=True):
    __tablename__ = "calibration"

    camera_id: int = Field(
        sa_column=Column("camera_id", Integer, ForeignKey("camera.id"), nullable=False)
    )

    timestamp: float = Field(
        sa_column=Column("timestamp", DECIMAL(17, 10), nullable=False)
    )

    resolution: float
    EMCuv: Optional[float] = None
    EMCxy: Optional[float] = None
    NCE: Optional[float] = None

    # Relaciones
    camera: Optional["Camera"] = Relationship(
        back_populates="calibrations"
    )

    rectified_images: List["RectifiedImage"] = Relationship(back_populates="calibration")
    picked_gcps: list["PickedGCP"] = Relationship(back_populates="calibration")
    parameters: list["CalibrationParameter"] = Relationship(back_populates="calibration")
    rois: list["ROI"] = Relationship(back_populates="calibration")



