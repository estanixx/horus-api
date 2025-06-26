from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer
from typing import Optional
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .fusion import Fusion
    from .fusionvalue import FusionValue


class FusionParameter(BaseSQLModel, table=True):
    __tablename__ = "fusion_parameter"

    id_fusion: int = Field(
        sa_column=Column("id_fusion", Integer, nullable=False),
        foreign_key="fusion.id"
    )

    name: str = Field(sa_column=Column("name", String, nullable=False))

    fusion: Optional["Fusion"] = Relationship(back_populates="parameters")
    values: list["FusionValue"] = Relationship(back_populates="parameter")

