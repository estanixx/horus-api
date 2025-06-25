from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .calibration import Calibration
    from .gcp import GCP


class PickedGCP(SQLModel, table=True):
    __tablename__ = "pickedgcp"

    calibration_id: str = Field(
        sa_column=Column(
            "calibration",
            String,
            ForeignKey("calibration.icalibration"),
            primary_key=True,
            nullable=False
        )
    )

    gcp_id: int = Field(
        sa_column=Column("gcp", Integer, nullable=False),
        primary_key=True
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False),
        primary_key=True
    )

    u: float
    v: float

    calibration: Optional["Calibration"] = Relationship(back_populates="picked_gcps")

    gcp: Optional["GCP"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(PickedGCP.gcp_id==GCP.idgcp, PickedGCP.station==GCP.station)",
            "foreign_keys": "[PickedGCP.gcp_id, PickedGCP.station]",
        },
        back_populates="picked_gcps"
    )
