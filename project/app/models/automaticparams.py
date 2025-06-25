from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .station import Station


class AutomaticParams(SQLModel, table=True):
    __tablename__ = "automaticparams"

    idauto: int = Field(
        sa_column=Column("idauto", Integer, nullable=False),
        primary_key=True
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False),
        foreign_key="station.name"
    )

    type: str = Field(sa_column=Column("type", String, nullable=False))

    start_hour: int
    start_minute: int
    end_hour: int
    end_minute: int

    step: int
    duration: Optional[int] = None
    num_images: Optional[int] = None

    station_ref: Optional["Station"] = Relationship(back_populates="automatic_params")
