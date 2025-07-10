from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .imagetype import ImageType
class Image(BaseSQLModel, table=True):

    filename: str = Field(
        unique=True,
        description="Name of the file"
    )
    image_type_id: Optional[int] = Field(
        nullable=False,
        foreign_key="image_type.id",
        description="Foreign key to a ImageType entity, stores the type of the image"
    )
    ismini: bool = Field(description="If the image is a miniature")
    path: str = Field(description="The path of the image")
    timestamp: float = Field(description="Time of the image")

    

    

    

