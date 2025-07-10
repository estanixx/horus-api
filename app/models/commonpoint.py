from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey
from sqlalchemy import String, Float, Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .fusion import Fusion
    from .camera import Camera


class CommonPoint(BaseSQLModel, table=True):
    __tablename__ = "common_point"

    id_fusion: int = Field(
        sa_column=Column("id_fusion", Integer, ForeignKey("fusion.id"), nullable=False),
        primary_key=True
    )

    camera_id: int = Field(
        sa_column=Column("camera", Integer, ForeignKey("camera.id"), nullable=False),
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
        back_populates="common_points"
    )
