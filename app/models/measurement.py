from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Integer, String, DECIMAL
from typing import Optional, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .measurementtype import MeasurementType
    from .measurementvalue import MeasurementValue


class Measurement(SQLModel, table=True):
    __tablename__ = "measurement"

    idmeasurement: int = Field(
        sa_column=Column("idmeasurement", Integer, primary_key=True, autoincrement=True, nullable=False)
    )

    station: str = Field(
        sa_column=Column("station", String, primary_key=True, nullable=False)
    )

    type_id: int = Field(
        sa_column=Column("type", Integer, nullable=False)
    )

    timestamp: float = Field(
        sa_column=Column("timestamp", DECIMAL(17, 10), nullable=False)
    )

    # Relaciones
    measurement_type: Optional["MeasurementType"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(Measurement.type_id==MeasurementType.id, "
                           "Measurement.station==MeasurementType.station)",
            "foreign_keys": "[Measurement.type_id, Measurement.station]"
        },
        back_populates="measurements"
    )

    values: List["MeasurementValue"] = Relationship(back_populates="measurement")
