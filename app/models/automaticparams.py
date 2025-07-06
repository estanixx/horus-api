from sqlmodel import Field, Relationship, Column
from sqlalchemy import String, Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .station import Station

class AutomaticParams(BaseSQLModel, table=True):
   
    station_id: str = Field(
        sa_column=Column("station", Integer, nullable=False),
        foreign_key="station.id"
    )
    type: str = Field(sa_column=Column("type", String, nullable=False))
    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int
    step: int
    duration: Optional[int] = None
    num_images: Optional[int] = None

    station: Optional["Station"] = Relationship(back_populates="automatic_params")
 