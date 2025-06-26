# app/models/obliqueimage.py

from sqlmodel import Field, Relationship, Column
from sqlalchemy import Integer
from typing import Optional, TYPE_CHECKING
from .image import Image
if TYPE_CHECKING:
    from .camera import Camera

class ObliqueImage(Image, table=True):
    __tablename__ = "oblique_image"

    camera_id: int = Field(
        sa_column=Column("camera", Integer, nullable=False),
        primary_key=False
    )

    # Relationships (opcional y condicional)
    camera: Optional["Camera"] = Relationship(
        back_populates="oblique_images"
    )