from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import Integer
from typing import Optional, TYPE_CHECKING
from .image import Image

if TYPE_CHECKING:
    from .camera import Camera
    from .imagetype import ImageType

class ObliqueImage(Image, table=True):
    __tablename__ = 'oblique_image'
    
    camera_id: int = Field(
        sa_column=Column("camera_id", Integer, ForeignKey('camera.id'), nullable=False),
    )
    image_type_id: Optional[int] = Field(
        sa_column=Column("image_type_id", Integer, ForeignKey('image_type.id'), nullable=False),
    )
    image_type: Optional["ImageType"] = Relationship(back_populates="oblique_images")
    camera: Optional["Camera"] = Relationship(
        back_populates="oblique_images"
    )