from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Column, ForeignKey, Integer
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .imagetype import ImageType
class Image(BaseSQLModel, table=False):

    filename: str = Field(
        unique=True,
        description="Name of the file"
    )

    ismini: bool = Field(description="If the image is a miniature")
    path: str = Field(description="The path of the image")
    timestamp: float = Field(description="Time of the image")

    

    

    

