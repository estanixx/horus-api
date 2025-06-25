from typing import List, Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .camera import Camera
    from .sensor import Sensor
    from .gcp import GCP
    from .automaticparams import AutomaticParams

class Station(BaseSQLModel, table=True):
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

    cameras: List["Camera"] = Relationship(back_populates="station")
    sensors: List["Sensor"] = Relationship(back_populates="station")
    gcps: List["GCP"] = Relationship(back_populates="station_ref")
    automatic_params: List["AutomaticParams"] = Relationship(back_populates="station_ref")

    def __repr__(self):
        return f"Station(id={self.id}, alias='{self.alias}', city='{self.city}')"