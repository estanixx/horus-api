from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, DECIMAL, Float
from typing import Optional, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .camera import Camera
    from .rectifiedimage import RectifiedImage
    from .pickedgcp import PickedGCP
    from .calibrationparameter import CalibrationParameter
    from .roi import ROI

class Calibration(SQLModel, table=True):
    __tablename__ = "calibration"

    idcalibration: str = Field(
        sa_column=Column("idcalibration", String, nullable=False),
        primary_key=True
    )

    camera_id: str = Field(
        sa_column=Column("camera", String, nullable=False)
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False)
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
        sa_relationship_kwargs={
            "primaryjoin": "and_(Calibration.camera_id==Camera.id, Calibration.station==Camera.station)",
            "foreign_keys": "[Calibration.camera_id, Calibration.station]",
        },
        back_populates="calibrations"
    )

    rectified_images: List["RectifiedImage"] = Relationship(back_populates="calibration")
    picked_gcps: list["PickedGCP"] = Relationship(back_populates="calibration")
    parameters: list["CalibrationParameter"] = Relationship(back_populates="calibration")
    rois: list["ROI"] = Relationship(back_populates="calibration")



