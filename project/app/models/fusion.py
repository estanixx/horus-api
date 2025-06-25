from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import String, DECIMAL
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .camerabyfusion import CameraByFusion
    from .fusionparameter import FusionParameter
    from .mergedimage import MergedImage
    from .commonpoint import CommonPoint

class Fusion(SQLModel, table=True):
    __tablename__ = "fusion"

    id: str = Field(
        sa_column=Column("id", String, nullable=False),
        primary_key=True
    )

    timestamp: float = Field(
        sa_column=Column("timestamp", DECIMAL(17, 10), nullable=False)
    )

    type: str = Field(sa_column=Column("type", String, nullable=False))

    cameras: List["CameraByFusion"] = Relationship(back_populates="fusion")
    parameters: List["FusionParameter"] = Relationship(back_populates="fusion")
    merged_images: List["MergedImage"] = Relationship(back_populates="fusion")
    common_points: List["CommonPoint"] = Relationship(back_populates="fusion")



