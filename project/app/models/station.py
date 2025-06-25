# app/models/station.py
"""
Station Database Model Definition.

This module defines the `Station` SQLModel class, which corresponds to the
'station' table in the database. It includes attributes for the station's
location and metadata, and defines its one-to-many relationship with the
`Camera` model.
"""

from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel

# The 'if TYPE_CHECKING:' block allows type checkers (like MyPy) and IDEs to
# import the 'Camera' model for autocompletion and type validation, but
# prevents a circular import error at runtime because the import is not
# actually executed when the Python interpreter runs the code.
if TYPE_CHECKING:
    from .camera import Camera
    from.sensor import Sensor
    from .gcp import GCP
    from .automaticparams import AutomaticParams


class Station(BaseSQLModel, table=True):
    """
    Represents a weather station record in the database.

    Inherits common fields (`id`, `created_at`, `updated_at`) from `BaseSQLModel`.

    Attributes:
        alias (str): A unique, human-readable identifier for the station.
        elevation (float): The station's elevation in meters.
        lat (float): The latitude coordinate of the station.
        lon (float): The longitude coordinate of the station.
        country (str): The country where the station is located.
        state (str): The state or province.
        city (str): The city.
        responsible (Optional[str]): The person or entity responsible for the station.
        description (Optional[str]): A free-text description of the station.
        cameras (List[Camera]): A list of all `Camera` objects linked to this station.
                                This is the ORM relationship.
    """
    alias: str = Field(
        unique=True,
        index=True,
        description="A unique, human-readable identifier for the station."
    )
    elevation: float = Field(description="The station's elevation above sea level, in meters.")
    lat: float = Field(description="The latitude of the station's geographical location.")
    lon: float = Field(description="The longitude of the station's geographical location.")
    country: str = Field(description="The country where the station is located.")
    state: str = Field(description="The state or province where the station is located.")
    city: str = Field(description="The city where the station is located.")
    responsible: Optional[str] = Field(default=None, description="The person or entity responsible for the station.")
    description: Optional[str] = Field(default=None, description="A free-text description of the station.")

    # This defines the one-to-many relationship in the Python code.
    # `back_populates="station"` connects this to the 'station' relationship in the Camera
    # model, ensuring that both sides of the relationship are kept in sync.
    cameras: List["Camera"] = Relationship(back_populates="station")
    sensors: list["Sensor"] = Relationship(back_populates="station_ref")
    gcps: list["GCP"] = Relationship(back_populates="station_ref")
    automatic_params: list["AutomaticParams"] = Relationship(back_populates="station_ref")


    def __repr__(self):
        """Provides a developer-friendly string representation of the Station object."""
        return f"Station(id={self.id}, alias='{self.alias}', city='{self.city}')"