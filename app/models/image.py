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
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .imagetype import ImageType
    from .rectifiedimage import RectifiedImage
    from .mergedimage import MergedImage

class Image(SQLModel, table=True):
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
        primary_key=True,
        description="Name of the file"
    )

    # CORRECTED: Switched to timezone-aware datetimes to prevent database errors.
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column=Column(
            TIMESTAMP(timezone=True),  # Ensures the database column type is TIMESTAMPTZ.
            nullable=False
        ),
        description="Timestamp of when the record was created (UTC)."
    )

    # CORRECTED: Switched to timezone-aware datetimes and combined SQLAlchemy arguments.
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            onupdate=lambda: datetime.now(timezone.utc)  # This tells the DB to update on modification.
        ),
        description="Timestamp of the last update to the record (UTC)."
    )
    idtype: Optional[str] = Field(
        sa_column=Column("type", nullable=False),
        foreign_key="imagetype.idtype",
        description="Foreign key to a ImageType entity, stores the type of the image"
    )

    imagetype: Optional["ImageType"] = Relationship(back_populates="images")

    timestamp: float = Field(description="Time of the image")

    ismini: bool = Field(description="If the image is a miniature")

    path: str = Field(description="The path of the image")

    rectified: Optional["RectifiedImage"] = Relationship(back_populates="image")
    merged: Optional["MergedImage"] = Relationship(back_populates="image")


    class Config:
        """Pydantic model configuration."""
        # Allows the model to use custom types that might not be natively supported by Pydantic.
        arbitrary_types_allowed = True