from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion import Fusion
    from .fusionvalue import FusionValue


class FusionParameter(SQLModel, table=True):
    __tablename__ = "fusionparameter"

    id: str = Field(
        sa_column=Column("id", String, nullable=False,
        primary_key=True)
    )

    idfusion: str = Field(
        sa_column=Column("idfusion", String, nullable=False),
        foreign_key="fusion.id"
    )

    name: str = Field(sa_column=Column("name", String, nullable=False))

    fusion: Optional["Fusion"] = Relationship(back_populates="parameters")
    values: list["FusionValue"] = Relationship(back_populates="parameter")

