from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey
from sqlalchemy import String, ForeignKey, Integer
from typing import Optional, TYPE_CHECKING
from .image import Image

if TYPE_CHECKING:
    from .fusion import Fusion
    from .imagetype import ImageType


class MergedImage(Image, table=True):
    __tablename__ = "merged_image"

    image_type: Optional["ImageType"] = Relationship(back_populates="merged_images")
    
    fusion_id: int = Field(
        sa_column=Column(
            "fusion_id",
            Integer,
            ForeignKey('fusion.id'),
            nullable=False,
        )
    )

    fusion: Optional["Fusion"] = Relationship(back_populates="merged_images")

    
