from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, Relationship
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .station import Station

class Camera(BaseSQLModel, table=True):
    reference: str = Field(index=True, description="A user-defined reference name for the camera.")
    sizeX: int = Field(description="The horizontal resolution (width) in pixels.")
    sizeY: int = Field(description="The vertical resolution (height) in pixels.")
    station_id: Optional[int] = Field(
        default=None,
        foreign_key="station.id",
        description="The foreign key of the station this camera belongs to."
    )

    station: Optional["Station"] = Relationship(back_populates="cameras")

    def __repr__(self):
        return f"Camera(id={self.id}, reference='{self.reference}', station_id={self.station_id})"