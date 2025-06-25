# app/models/camera.py
"""
Camera Database Model Definition.

This module defines the `Camera` SQLModel class, which corresponds to the
'camera' table in the database. It includes attributes for the camera's
specifications and defines its relationship to the `Station` model.
"""

from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel

# The 'if TYPE_CHECKING:' block allows type checkers (like MyPy) and IDEs to
# import the 'Station' model for autocompletion and type validation, but
# prevents a circular import error at runtime because the import is not
# actually executed when the Python interpreter runs the code.
if TYPE_CHECKING:
    from .station import Station


class Camera(BaseSQLModel, table=True):
    """
    Represents a camera record in the database.

    Inherits common fields (`id`, `created_at`, `updated_at`) from `BaseSQLModel`.

    Attributes:
        reference (str): A user-defined reference for the camera. Indexed for performance.
        sizeX (int): The horizontal resolution (width) of the camera's sensor in pixels.
        sizeY (int): The vertical resolution (height) of the camera's sensor in pixels.
        station_id (int): The foreign key linking this camera to a record in the 'station' table.
        station (Station): The ORM relationship to the parent Station object. This allows
                         accessing the full Station object from a Camera instance
                         (e.g., `my_camera.station`).
    """
    reference: str = Field(index=True, description="A user-defined reference name for the camera.")
    sizeX: int = Field(description="The horizontal resolution (width) in pixels.")
    sizeY: int = Field(description="The vertical resolution (height) in pixels.")

    # This field defines the foreign key relationship at the database level.
    station_id: Optional[int] = Field(
        default=None,
        foreign_key="station.id",
        description="The foreign key of the station this camera belongs to."
    )

    # This defines the object-oriented relationship in the Python code.
    # `back_populates="cameras"` connects this to the 'cameras' list in the Station
    # model, ensuring that both sides of the relationship are kept in sync.
    station: Optional["Station"] = Relationship(back_populates="cameras")

    def __repr__(self):
        """Provides a developer-friendly string representation of the Camera object."""
        return f"Camera(id={self.id}, reference='{self.reference}', station_id={self.station_id})"