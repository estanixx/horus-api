from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import Sensor
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from app.graphql.types import SensorCreateInput

class SensorService:
    """Service class for sensor-related operations."""

    @staticmethod
    async def get_by_id(db: AsyncSession, sensor_id: int) -> Optional[Sensor]:
        """
        Retrieves a single sensor by its ID, pre-loading the parent station.
        """
        statement = (
            select(Sensor)
            .where(Sensor.id == sensor_id)
        )
        result = await db.exec(statement)
        return result.first()

    @staticmethod
    async def get_for_station(
        db: AsyncSession, station_id: int, skip: int, limit: int
    ) -> Tuple[List[Sensor], int]:
        """
        Retrieves a paginated list of sensors for a specific station and the total count.
        """
        statement = (
            select(Sensor)
            .where(Sensor.station_id == station_id)
            .offset(skip)
            .limit(limit)
        )
        result = await db.exec(statement)
        sensors = result.all()
        
        count_statement = select(func.count()).select_from(Sensor).where(Sensor.station_id == station_id)
        total_count = (await db.exec(count_statement)).one()
        
        return sensors, total_count

    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[Sensor], int]:
        """
        Retrieves a paginated list of all sensors.
        """
        statement = select(Sensor).offset(skip).limit(limit)
        result = await db.exec(statement)
        sensors = result.all()

        count_statement = select(func.count()).select_from(Sensor)
        total_count = (await db.exec(count_statement)).one()

        return sensors, total_count

    @staticmethod
    async def create(db: AsyncSession, data:  Annotated["SensorCreateInput", strawberry.lazy('app.graphql.types')]) -> Sensor: # Or SensorCreateInput
        """Creates a new camera."""
        # Explicitly convert the input object to a dictionary for validation
        new_model = Sensor(**strawberry.asdict(data))
        
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @staticmethod
    async def update(db: AsyncSession, sensor_id: int, data:  Annotated["SensorCreateInput", strawberry.lazy('app.graphql.types')]) -> Optional[Sensor]:
        """Updates an existing sensor."""
        sensor = await db.get(Sensor, sensor_id)
        if not sensor:
            return None

        update_data = strawberry.asdict(data)
        for key, value in update_data.items():
            setattr(sensor, key, value)

        db.add(sensor)
        await db.commit()
        await db.refresh(sensor)
        return sensor

    @staticmethod
    async def delete(db: AsyncSession, sensor_id: int) -> Optional[Sensor]:
        """Deletes a sensor."""
        sensor = await db.get(Sensor, sensor_id)
        if not sensor:
            return None
        
        await db.delete(sensor)
        await db.commit()
        return sensor