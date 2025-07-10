from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import Integer
from typing import Optional
from typing import TYPE_CHECKING
from .image import Image

if TYPE_CHECKING:
    from .calibration import Calibration
    from .imagetype import ImageType


class RectifiedImage(Image, table=True):

    image_type: Optional["ImageType"] = Relationship(back_populates="rectified_images")
    
    calibration_id: int = Field(
        sa_column=Column("calibration_id", Integer, ForeignKey("calibration.id"),  nullable=False),
    )

    calibration: Optional["Calibration"] = Relationship(back_populates="rectified_images")
    