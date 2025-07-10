from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import String, Integer, Float, DECIMAL
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .camera import Camera

class TimeStack(BaseSQLModel, table=True):

    filename: str = Field(
        sa_column=Column(
            "filename",
            String,
            primary_key=True,
            nullable=False
        )
    )
    camera_id: int = Field(
        sa_column=Column("camera_id", Integer, ForeignKey("camera.id"), nullable=True),
        
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

    
    camera: Optional["Camera"] = Relationship(
        back_populates="timestacks"
    )
