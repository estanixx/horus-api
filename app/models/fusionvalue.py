from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import TimestampsSQLModel

if TYPE_CHECKING:
    from .fusionparameter import FusionParameter


class FusionValue(TimestampsSQLModel, table=True):
    __tablename__ = "fusion_value"

    id_matrix: int = Field(
        sa_column=Column("id_matrix", Integer, ForeignKey("fusion_parameter.id"), nullable=False,
        primary_key=True,
        )
    )

    id_col: int = Field(
        sa_column=Column("id_col", Integer, nullable=False,
        primary_key=True)
    )

    id_row: int = Field(
        sa_column=Column("id_row", Integer, nullable=False,
        primary_key=True)
    )

    value: float = Field(
        sa_column=Column("value", Float, nullable=False)
    )

    parameter: Optional["FusionParameter"] = Relationship(back_populates="values")
