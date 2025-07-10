from typing import List, Optional, TYPE_CHECKING
from app.models.base import BaseSQLModel
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from .obliqueimage import ObliqueImage
    from .mergedimage import MergedImage
    from .rectifiedimage import RectifiedImage 

class ImageType(BaseSQLModel, table=True):
    name: str = Field(description="The name of the type")
    description: Optional[str] = Field(description="A brief description of the type")

    oblique_images: List["ObliqueImage"] = Relationship(back_populates="image_type")
    merged_images: List["MergedImage"] = Relationship(back_populates="image_type")
    rectified_images: List["RectifiedImage"] = Relationship(back_populates="image_type")
