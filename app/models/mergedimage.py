from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import ForeignKey, Integer
from typing import Optional, TYPE_CHECKING
from .image import Image

if TYPE_CHECKING:
    from .fusion import Fusion
    from .imagetype import ImageType

class MergedImage(Image, table=True):
    
    fusion_id: int = Field(
        sa_column=Column(
            "fusion_id",
            Integer,
            ForeignKey('fusion.id'),
            nullable=False,
        )
    )

    fusion: Optional["Fusion"] = Relationship(back_populates="merged_images")
    image_type: Optional["ImageType"] = Relationship(back_populates="merged_images")

    
