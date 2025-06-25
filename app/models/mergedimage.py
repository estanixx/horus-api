from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, ForeignKey
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion import Fusion
    from .image import Image


class MergedImage(SQLModel, table=True):
    __tablename__ = "mergedimage"

    filename: str = Field(
        sa_column=Column(
            "filename",
            String,
            ForeignKey("image.filename"),
            primary_key=True,
            nullable=False
        )
    )

    idfusion: str = Field(
        sa_column=Column(
            "idfusion",
            String,
            ForeignKey("fusion.id"),
            nullable=False
        )
    )

    image: Optional["Image"] = Relationship(back_populates="merged")
    fusion: Optional["Fusion"] = Relationship(back_populates="merged_images")


    
