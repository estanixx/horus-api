from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .fusion import Fusion
    from .camera import Camera

class CameraByFusion(BaseSQLModel, table=True):

    fusion_id: int = Field(
        sa_column=Column("fusion_id", Integer, ForeignKey("fusion.id"), nullable=False, primary_key=True),
    )
    camera_id: int = Field(
        sa_column=Column("camera_id", Integer, ForeignKey("camera.id"), nullable=False,
        primary_key=True),
    )
    sequence: int = Field(
        sa_column=Column("sequence", Integer, nullable=False)
    )

    fusion: Optional["Fusion"] = Relationship(back_populates="cameras")
    camera: Optional["Camera"] = Relationship(
        back_populates="fusions"
    )
