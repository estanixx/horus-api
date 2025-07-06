from sqlmodel import Field, Relationship, Column
from sqlalchemy import String, Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .calibration import Calibration
    from .gcp import GCP


class PickedGCP(BaseSQLModel, table=True):

    calibration_id: str = Field(
        sa_column=Column(
            "calibration",
            String,
            primary_key=True,
            nullable=False
        ),
        foreign_key="calibration.id",
    )
    gcp_id: int = Field(
        sa_column=Column("gcp_id", Integer, nullable=False),
        primary_key=True,
        foreign_key="gcp.id"
    )
    u: float
    v: float

    calibration: Optional["Calibration"] = Relationship(back_populates="picked_gcps")
    gcp: Optional["GCP"] = Relationship(
        back_populates="picked_gcps"
    )
