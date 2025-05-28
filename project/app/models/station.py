# app/models/station.py
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel # Assuming this path

if TYPE_CHECKING:
    from .camera import Camera # For type checking (IDE autocompletion)

class Station(BaseSQLModel, table=True):
    # Added 'id' as a primary key, which is common for most models.
    # If 'alias' is intended to be the primary key, adjust accordingly.
    id: Optional[int] = Field(default=None, primary_key=True)
    alias: str = Field(unique=True, index=True) # Added unique and index for alias
    elevation: float
    lat: float
    lon: float
    country: str
    state: str
    city: str
    responsible: Optional[str] = None
    description: Optional[str] = None

    # Relationship to Camera. Use "Camera" as string for runtime,
    # and Camera type for TYPE_CHECKING
    cameras: List["Camera"] = Relationship(back_populates="station")

    def __repr__(self):
        return f"Station(id={self.id}, alias='{self.alias}', city='{self.city}')"