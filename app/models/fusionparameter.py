from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey
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
        sa_column=Column("id_fusion", Integer, ForeignKey("fusion.id"), nullable=False),       
    )

    name: str = Field(sa_column=Column("name", String, nullable=False))

    fusion: Optional["Fusion"] = Relationship(back_populates="parameters")
    values: list["FusionValue"] = Relationship(back_populates="parameter")

