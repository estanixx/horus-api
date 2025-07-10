# app/models/image.py
"""
Base SQLModel Definition.

This module defines a `BaseSQLModel` class that serves as the foundation for
all other database models in the application. It includes common, automatically
managed fields such as `id`, `created_at`, and `updated_at`.
"""

from datetime import datetime, timezone
from typing import Optional, TYPE_CHECKING

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlmodel import Field, Relationship, SQLModel, Integer
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .imagetype import ImageType
class Image(BaseSQLModel, table=False):
    """
    Represents a image record in the database.

    Attributes:
        filename (str): The primary key for the record. Auto-populated by the database.
        created_at (datetime): Timestamp of when the record was created. Auto-populated.
        updated_at (datetime): Timestamp of the last update. Auto-updated by the database.
        idtype (str): Foreign key to a ImageType entity, stores the type of the image (e.g snap, timex, var)
        timestamp (double): Time of the image 
        is_mini (bool): Shows if the image is a miniature
        path (str): the path of the image
    """
    filename: str = Field(
        unique=True,
        description="Name of the file"
    )

    image_type_id: Optional[int] = Field(
        nullable=False,
        foreign_key="image_type.id",
        description="Foreign key to a ImageType entity, stores the type of the image"
    )

    

    timestamp: float = Field(description="Time of the image")

    ismini: bool = Field(description="If the image is a miniature")

    path: str = Field(description="The path of the image")

