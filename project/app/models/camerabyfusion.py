from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion import Fusion
    from .camera import Camera


class CameraByFusion(SQLModel, table=True):
    __tablename__ = "camerabyfusion"

    idfusion: str = Field(
        sa_column=Column("idfusion", String, ForeignKey("fusion.id"), nullable=False,
        primary_key=True,
        )
    )

    camera_id: str = Field(
        sa_column=Column("camera", String, nullable=False,
        primary_key=True)
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False,
        primary_key=True)
    )

    sequence: int = Field(
        sa_column=Column("sequence", Integer, nullable=False)
    )

    fusion: Optional["Fusion"] = Relationship(back_populates="cameras")

    camera: Optional["Camera"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(CameraByFusion.camera_id==Camera.id, "
                           "CameraByFusion.station==Camera.station)",
            "foreign_keys": "[CameraByFusion.camera_id, CameraByFusion.station]"
        },
        back_populates="fusions"
    )
