from sqlmodel import Field, Relationship, Column
from sqlalchemy import Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .fusion import Fusion
    from .camera import Camera

class CameraByFusion(BaseSQLModel, table=True):

    id_fusion: int = Field(
        sa_column=Column("id_fusion", Integer, nullable=False, primary_key=True),
        foreign_key="fusion.id",
    )
    camera_id: int = Field(
        sa_column=Column("camera", Integer, nullable=False,
        primary_key=True),
        foreign_key="camera.id",
    )
    sequence: int = Field(
        sa_column=Column("sequence", Integer, nullable=False)
    )

    fusion: Optional["Fusion"] = Relationship(back_populates="cameras")
    camera: Optional["Camera"] = Relationship(
        back_populates="fusions"
    )
