# app/models/obliqueimage.py

from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, ForeignKey
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .image import Image
    from .camera import Camera

class ObliqueImage(SQLModel, table=True):
    __tablename__ = "obliqueimage"

    filename: str = Field(
        sa_column=Column(
            "filename",
            String,
            ForeignKey("image.filename"),
            primary_key=True,
            nullable=False
        )
    )

    camera_id: str = Field(
        sa_column=Column("camera", String, nullable=False),
        primary_key=False
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False),
        primary_key=False
    )

    # Relationships (opcional y condicional)
    image: Optional["Image"] = Relationship(back_populates="oblique")
    camera: Optional["Camera"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(ObliqueImage.camera_id==Camera.id, ObliqueImage.station==Camera.station)",
            "foreign_keys": "[ObliqueImage.camera_id, ObliqueImage.station]",
        },
        back_populates="oblique_images"
    )