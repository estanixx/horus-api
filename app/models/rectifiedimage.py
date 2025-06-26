# app/models/rectifiedimage.py
from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, ForeignKey, Integer
from typing import Optional
from typing import TYPE_CHECKING
from .image import Image

if TYPE_CHECKING:
    from .calibration import Calibration


class RectifiedImage(Image, table=True):
    __tablename__ = "rectified_image"

    calibration_id: int = Field(
        sa_column=Column("calibration", Integer, nullable=False),
        foreign_key="calibration.id"
    )

    calibration: Optional["Calibration"] = Relationship(back_populates="rectified_images")
    