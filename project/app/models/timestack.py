from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer, Float, DECIMAL, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .camera import Camera


class TimeStack(SQLModel, table=True):
    __tablename__ = "timestack"

    filename: str = Field(
        sa_column=Column(
            "filename",
            String,
            primary_key=True,
            nullable=False
        )
    )

    camera_id: str = Field(
        sa_column=Column("camera", String, nullable=False)
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False)
    )

    inittime: float = Field(
        sa_column=Column("inittime", DECIMAL(17, 10), nullable=False)
    )

    path: str = Field(
        sa_column=Column("path", String, nullable=False)
    )

    fps: float = Field(
        sa_column=Column("fps", Float, nullable=False)
    )

    numFrames: int = Field(
        sa_column=Column("numFrames", Integer, nullable=False)
    )

    # Relaciones
    camera: Optional["Camera"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(TimeStack.camera_id==Camera.id, TimeStack.station==Camera.station)",
            "foreign_keys": "[TimeStack.camera_id, TimeStack.station]"
        },
        back_populates="timestacks"
    )
