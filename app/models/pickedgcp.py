from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import String, Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .calibration import Calibration
    from .gcp import GCP


class PickedGCP(BaseSQLModel, table=True):

    calibration_id: int = Field(
        sa_column=Column(
            "calibration",
            Integer,
            ForeignKey("calibration.id"),
            primary_key=True,
            nullable=False
        ),
        
    )
    gcp_id: int = Field(
        sa_column=Column("gcp_id", Integer, ForeignKey("gcp.id"), nullable=False),
        primary_key=True,
    )
    u: float
    v: float

    calibration: Optional["Calibration"] = Relationship(back_populates="picked_gcps")
    gcp: Optional["GCP"] = Relationship(
        back_populates="picked_gcps"
    )
