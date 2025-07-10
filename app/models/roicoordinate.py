from sqlmodel import Field, Relationship, Column
from sqlalchemy import Integer, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .roi import ROI


class ROICoordinate(BaseSQLModel, table=True):
   
    roi_id: int = Field(
        sa_column=Column(
            "roi_id",
            Integer,
            ForeignKey("roi.id"),
            nullable=False,
            primary_key=True
        )
    )
    u: float
    v: float

    roi: Optional["ROI"] = Relationship(back_populates="coordinates")
