from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import Integer, Float
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .measurement import Measurement


class MeasurementValue(BaseSQLModel, table=True):
    __tablename__ = 'measurement_value'

    measurement_id: int = Field(
        sa_column=Column("measurement_id", Integer, ForeignKey("measurement.id"),  nullable=False,
        primary_key=True),
        
    )


    id_col: int = Field(
        sa_column=Column("id_col", Integer, nullable=False,
        primary_key=True)
    )

    id_row: int = Field(
        sa_column=Column("id_row", Integer, nullable=False,
        primary_key=True)
    )

    id_depth: int = Field(
        sa_column=Column("id_depth", Integer, nullable=False,
        primary_key=True)
    )

    value: float = Field(
        sa_column=Column("value", Float, nullable=False)
    )

    measurement: Optional["Measurement"] = Relationship(
        back_populates="values"
    )
