from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import Measurement

class MeasurementService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[Measurement], int]:
        statement = select(Measurement).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(Measurement)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, measurement_id: int) -> Optional[Measurement]:
        return await db.get(Measurement, measurement_id)

    @staticmethod
    async def get_for_station(db: AsyncSession, station_id: int, skip: int, limit: int) -> Tuple[List[Measurement], int]:
        statement = select(Measurement).where(Measurement.station_id == station_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(Measurement).where(Measurement.station_id == station_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_for_measurement_type(db: AsyncSession, type_id: int, skip: int, limit: int) -> Tuple[List[Measurement], int]:
        statement = select(Measurement).where(Measurement.measurement_type_id == type_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(Measurement).where(Measurement.measurement_type_id == type_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: Measurement) -> Measurement:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, measurement_id: int, update_data: dict) -> Optional[Measurement]:
        item = await db.get(Measurement, measurement_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, measurement_id: int) -> Optional[Measurement]:
        item = await db.get(Measurement, measurement_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item