from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import ForeignKey, Integer
from typing import Optional, TYPE_CHECKING
from .image import Image

if TYPE_CHECKING:
    from .fusion import Fusion
    from .imagetype import ImageType

class MergedImage(Image, table=True):
    __tablename__ = 'merged_image'

    fusion_id: int = Field(
        sa_column=Column(
            "fusion_id",
            Integer,
            ForeignKey('fusion.id'),
            nullable=False,
        )
    )

    fusion: Optional["Fusion"] = Relationship(back_populates="merged_images")
    image_type_id: Optional[int] = Field(
        sa_column=Column("image_type_id", Integer, ForeignKey('image_type.id'), nullable=False),
    )
    image_type: Optional["ImageType"] = Relationship(back_populates="merged_images")

    
