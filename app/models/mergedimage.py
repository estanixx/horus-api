from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, ForeignKey
from typing import Optional, TYPE_CHECKING
from .image import Image

if TYPE_CHECKING:
    from .fusion import Fusion


class MergedImage(Image, table=True):
    __tablename__ = "merged_image"


    fusion_id: str = Field(
        foreign_key='fusion.id',
        sa_column=Column(
            "fusion_id",
            String,
            nullable=False
        )
    )

    fusion: Optional["Fusion"] = Relationship(back_populates="merged_images")

    
