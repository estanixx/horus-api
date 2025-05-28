# app/models/camera.py
from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel # Assuming this path

if TYPE_CHECKING:
    from .station import Station # For type checking (IDE autocompletion)

class Camera(BaseSQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=False, primary_key=True)
    reference: str = Field(index=True)
    sizeX: int
    sizeY: int

    # Foreign Key to Station
    station_id: int = Field(default=None, foreign_key="station.id")

    # Relationship to Station. Use "Station" as string for runtime,
    # and Station type for TYPE_CHECKING
    station: "Station" = Relationship(back_populates="cameras")

    def __repr__(self):
        return f"Camera(id={self.id}, reference='{self.reference}', station_id={self.station_id})"