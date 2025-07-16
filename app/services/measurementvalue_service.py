from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import MeasurementValue

class MeasurementValueService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[MeasurementValue], int]:
        statement = select(MeasurementValue).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(MeasurementValue)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_ids(db: AsyncSession, measurement_id: int, id_col: int, id_row: int, id_depth: int) -> Optional[MeasurementValue]:
        return await db.get(MeasurementValue, (measurement_id, id_col, id_row, id_depth))

    @staticmethod
    async def get_for_measurement(db: AsyncSession, measurement_id: int, skip: int, limit: int) -> Tuple[List[MeasurementValue], int]:
        statement = select(MeasurementValue).where(MeasurementValue.measurement_id == measurement_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(MeasurementValue).where(MeasurementValue.measurement_id == measurement_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: MeasurementValue) -> MeasurementValue:
        db.add(data)
        await db.commit()
        # Cannot refresh composite primary key objects yet
        return data

    @staticmethod
    async def update(db: AsyncSession, measurement_id: int, id_col: int, id_row: int, id_depth: int, update_data: dict) -> Optional[MeasurementValue]:
        item = await db.get(MeasurementValue, (measurement_id, id_col, id_row, id_depth))
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        return item

    @staticmethod
    async def delete(db: AsyncSession, measurement_id: int, id_col: int, id_row: int, id_depth: int) -> Optional[MeasurementValue]:
        item = await db.get(MeasurementValue, (measurement_id, id_col, id_row, id_depth))
        if item:
            await db.delete(item)
            await db.commit()
        return item