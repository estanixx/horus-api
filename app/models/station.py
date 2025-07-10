# app/models/station.py

from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

# The BaseSQLModel should be a simple SQLModel that includes an ID.
# If you don't have one, you can define it as:
# class BaseSQLModel(SQLModel):
#     id: Optional[int] = Field(default=None, primary_key=True)

from app.models.base import BaseSQLModel

# This block prevents circular imports at runtime by only importing types for type checking.
# It's crucial for models with relationships.
if TYPE_CHECKING:
    from .camera import Camera
    from .sensor import Sensor
    from .gcp import GCP
    from .automaticparams import AutomaticParams
    from .measurement import Measurement

class Station(BaseSQLModel, table=True):
    """
    Represents a physical monitoring station.

    A station is a specific geographical point where cameras, sensors, and other
    equipment are installed to monitor coastal conditions. This model stores the
    station's location, metadata, and links to all associated equipment and data.

    Attributes:
        id: The primary key for the station.
        alias: A unique, human-readable identifier for the station (e.g., "Copacabana_Posto_6").
        elevation: The station's elevation above sea level, in meters.
        lat: The latitude of the station's geographical location (WGS 84).
        lon: The longitude of the station's geographical location (WGS 84).
        country: The country where the station is located (e.g., "Brazil").
        state: The state or province where the station is located (e.g., "Rio de Janeiro").
        city: The city or nearest municipality to the station (e.g., "Rio de Janeiro").
        responsible: The person or entity responsible for maintaining the station.
        description: A free-text description of the station, its location, or its purpose.
        cameras: A list of Camera objects associated with this station.
        sensors: A list of Sensor objects associated with this station.
        gcps: A list of Ground Control Points (GCPs) defined for this station.
        automatic_params: A list of automatic parameter configurations for this station.
        measurements: A list of all measurements recorded by this station's sensors.
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

    # --- Relationships ---
    # The `Relationship` function defines the link to other models.
    # `back_populates` is essential for creating a two-way link between the models.
    cameras: List["Camera"] = Relationship(back_populates="station")
    sensors: List["Sensor"] = Relationship(back_populates="station")
    gcps: List["GCP"] = Relationship(back_populates="station")
    automatic_params: List["AutomaticParams"] = Relationship(back_populates="station")
    measurements: List["Measurement"] = Relationship(back_populates="station")

    def __repr__(self) -> str:
        """Provides a developer-friendly string representation of the Station object."""
        return f"Station(id={self.id}, alias='{self.alias}', city='{self.city}')"

