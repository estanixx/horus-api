from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .roi import ROI


class ROICoordinate(SQLModel, table=True):
    __tablename__ = "roicoordinate"

    idcoord: int = Field(
        sa_column=Column(
            "idcoord",
            Integer,
            autoincrement=True,
            nullable=False,
            primary_key=True
        )
    )

    idroi: str = Field(
        sa_column=Column(
            "idroi",
            String,
            ForeignKey("roi.idroi"),
            nullable=False,
            primary_key=True
        )
    )

    u: float
    v: float

    roi: Optional["ROI"] = Relationship(back_populates="coordinates")
