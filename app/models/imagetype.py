from typing import List, Optional, TYPE_CHECKING
from app.models.base import BaseSQLModel
from sqlmodel import Field, Relationship

if TYPE_CHECKING:
    from .image import Image

class ImageType(BaseSQLModel, table=True):
    name: str = Field(description="The name of the type")
    description: Optional[str] = Field(description="A brief description of the type")

    images: List["Image"] = Relationship(back_populates="image_type")
