from sqlmodel import SQLModel, Field, Relationship, Column, ForeignKey
from sqlalchemy import Integer, String, DECIMAL
from typing import Optional, List
from typing import TYPE_CHECKING
from app.models.base import BaseSQLModel


if TYPE_CHECKING:
    from .measurementtype import MeasurementType
    from .measurementvalue import MeasurementValue
    from .station import Station


class Measurement(BaseSQLModel, table=True):
    __tablename__ = "measurement"


    station_id: int = Field(
        sa_column=Column("station_id", Integer, ForeignKey("station.id"), nullable=False)
    )

    measurement_type_id: int = Field(
        sa_column=Column("type", Integer, ForeignKey("measurement_type.id"), nullable=False),
    )

    timestamp: float = Field(
        sa_column=Column("timestamp", DECIMAL(17, 10), nullable=False)
    )

    station: Optional["Station"] = Relationship(
        back_populates="measurements",
    )
    # Relaciones
    measurement_type: Optional["MeasurementType"] = Relationship(
        back_populates="measurements"
    )

    values: List["MeasurementValue"] = Relationship(back_populates="measurement")
