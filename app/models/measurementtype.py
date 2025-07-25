from sqlmodel import Field, Relationship, Column, ForeignKey
from sqlalchemy import Integer
from typing import Optional, List, TYPE_CHECKING
from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .sensor import Sensor
    from .measurement import Measurement


class MeasurementType(BaseSQLModel, table=True):
    __tablename__ = "measurement_type"

    sensor_id: int = Field(
        
        sa_column=Column("sensor_id", Integer, ForeignKey("sensor.id"), nullable=False)
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

    sensor: Optional["Sensor"] = Relationship(
        back_populates="measurement_types"
    )

    measurements: List["Measurement"] = Relationship(back_populates="measurement_type")
