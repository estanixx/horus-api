from sqlmodel import SQLModel, Field, Column, Relationship
from sqlalchemy import String, DECIMAL
from typing import List, TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .camerabyfusion import CameraByFusion
    from .fusionparameter import FusionParameter
    from .mergedimage import MergedImage
    from .commonpoint import CommonPoint

class Fusion(BaseSQLModel, table=True):
    __tablename__ = "fusion"

    timestamp: float = Field(
        sa_column=Column("timestamp", DECIMAL(17, 10), nullable=False)
    )
    
    fusion_type: str = Field(sa_column=Column("fusion_type", String, nullable=False))

    cameras: List["CameraByFusion"] = Relationship(back_populates="fusion")
    parameters: List["FusionParameter"] = Relationship(back_populates="fusion")
    merged_images: List["MergedImage"] = Relationship(back_populates="fusion")
    common_points: List["CommonPoint"] = Relationship(back_populates="fusion")



