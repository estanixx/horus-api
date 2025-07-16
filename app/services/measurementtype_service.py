from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import MeasurementType

class MeasurementTypeService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[MeasurementType], int]:
        statement = select(MeasurementType).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(MeasurementType)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, type_id: int) -> Optional[MeasurementType]:
        return await db.get(MeasurementType, type_id)

    @staticmethod
    async def get_for_sensor(db: AsyncSession, sensor_id: int, skip: int, limit: int) -> Tuple[List[MeasurementType], int]:
        statement = select(MeasurementType).where(MeasurementType.sensor_id == sensor_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(MeasurementType).where(MeasurementType.sensor_id == sensor_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: MeasurementType) -> MeasurementType:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, type_id: int, update_data: dict) -> Optional[MeasurementType]:
        item = await db.get(MeasurementType, type_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, type_id: int) -> Optional[MeasurementType]:
        item = await db.get(MeasurementType, type_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item