from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import Integer, String, Float
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .measurement import Measurement


class MeasurementValue(SQLModel, table=True):
    __tablename__ = "measurementvalue"

    idmeasurement: int = Field(
        sa_column=Column("idmeasurement", Integer, nullable=False,
        primary_key=True)
    )

    station: str = Field(
        sa_column=Column("station", String, nullable=False,
        primary_key=True)
    )

    idcol: int = Field(
        sa_column=Column("idcol", Integer, nullable=False,
        primary_key=True)
    )

    idrow: int = Field(
        sa_column=Column("idrow", Integer, nullable=False,
        primary_key=True)
    )

    iddepth: int = Field(
        sa_column=Column("iddepth", Integer, nullable=False,
        primary_key=True)
    )

    value: float = Field(
        sa_column=Column("value", Float, nullable=False)
    )

    measurement: Optional["Measurement"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(MeasurementValue.idmeasurement==Measurement.idmeasurement, "
                           "MeasurementValue.station==Measurement.station)",
            "foreign_keys": "[MeasurementValue.idmeasurement, MeasurementValue.station]"
        },
        back_populates="values"
    )
