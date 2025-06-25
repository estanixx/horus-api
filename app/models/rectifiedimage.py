# app/models/rectifiedimage.py
from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .image import Image
    from .calibration import Calibration


class RectifiedImage(SQLModel, table=True):
    __tablename__ = "rectifiedimage"

    filename: str = Field(
        sa_column=Column(
            "filename",
            String,
            ForeignKey("image.filename"),
            primary_key=True,
            nullable=False
        )
    )

    calibration_id: str = Field(
        sa_column=Column("calibration", String, nullable=False),
        foreign_key="calibration.idcalibration"
    )

    image: Optional["Image"] = Relationship(back_populates="rectified")
    calibration: Optional["Calibration"] = Relationship(back_populates="rectified_images")
    