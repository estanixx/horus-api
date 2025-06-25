from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer, Float, ForeignKey
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fusionparameter import FusionParameter


class FusionValue(SQLModel, table=True):
    __tablename__ = "fusionvalue"

    idmatrix: str = Field(
        sa_column=Column("idmatrix", String, ForeignKey("fusionparameter.id"), nullable=False,
        primary_key=True,
        )
    )

    idcol: int = Field(
        sa_column=Column("idcol", Integer, nullable=False,
        primary_key=True)
    )

    idrow: int = Field(
        sa_column=Column("idrow", Integer, nullable=False,
        primary_key=True)
    )

    value: float = Field(
        sa_column=Column("value", Float, nullable=False)
    )

    parameter: Optional["FusionParameter"] = Relationship(back_populates="values")
