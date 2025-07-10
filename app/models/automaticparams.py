from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey
from sqlalchemy import String, Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel
if TYPE_CHECKING:
    from .station import Station


class AutomaticParams(BaseSQLModel, table=True):
    __tablename__ = "automatic_params"


    station_id: str = Field(
        sa_column=Column("station_id", Integer, ForeignKey("station.id"), nullable=False),
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
 