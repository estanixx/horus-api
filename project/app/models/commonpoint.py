from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Float
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion import Fusion
    from .camera import Camera


class CommonPoint(SQLModel, table=True):
    __tablename__ = "commonpoint"

    idfusion: str = Field(
        sa_column=Column("idfusion", String, nullable=False),
        primary_key=True,
        foreign_key="fusion.id"
    )

    camera_id: str = Field(
        sa_column=Column("camera", String, nullable=False),
        primary_key=True
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False),
        primary_key=True
    )

    name: str = Field(
        sa_column=Column("name", String, nullable=False),
        primary_key=True
    )

    u: float
    v: float

    fusion: Optional["Fusion"] = Relationship(back_populates="common_points")

    camera: Optional["Camera"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(CommonPoint.camera_id==Camera.id, CommonPoint.station==Camera.station)",
            "foreign_keys": "[CommonPoint.camera_id, CommonPoint.station]"
        },
        back_populates="common_points"
    )
