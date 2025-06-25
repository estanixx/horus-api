from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy import String, Integer
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .sensor import Sensor
    from .measurement import Measurement


class MeasurementType(SQLModel, table=True):
    __tablename__ = "measurementtype"

    id: int = Field(
        sa_column=Column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    )

    station: str = Field(
        sa_column=Column("station", String, primary_key=True, nullable=False)
    )

    sensor: str = Field(
        sa_column=Column("sensor", String, nullable=False)
    )

    paramname: str
    datatype: str

    unitx: Optional[str] = None
    unity: Optional[str] = None
    unitz: Optional[str] = None

    axisnamex: Optional[str] = None
    axisnamey: Optional[str] = None
    axisnamez: Optional[str] = None

    description: Optional[str] = None

    sensor_ref: Optional["Sensor"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "and_(MeasurementType.sensor==Sensor.name, MeasurementType.station==Sensor.station)",
            "foreign_keys": "[MeasurementType.sensor, MeasurementType.station]"
        },
        back_populates="measurement_types"
    )

    measurements: List["Measurement"] = Relationship(back_populates="measurement_type")
