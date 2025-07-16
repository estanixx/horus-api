from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import CalibrationValue

class CalibrationValueService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[CalibrationValue], int]:
        statement = select(CalibrationValue).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(CalibrationValue)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_ids(db: AsyncSession, id_param: int, id_col: int, id_row: int) -> Optional[CalibrationValue]:
        return await db.get(CalibrationValue, (id_param, id_col, id_row))

    @staticmethod
    async def get_for_parameter(db: AsyncSession, param_id: int, skip: int, limit: int) -> Tuple[List[CalibrationValue], int]:
        statement = select(CalibrationValue).where(CalibrationValue.id_param == param_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(CalibrationValue).where(CalibrationValue.id_param == param_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: CalibrationValue) -> CalibrationValue:
        db.add(data)
        await db.commit()
        # Cannot refresh composite primary key objects yet
        return data

    @staticmethod
    async def update(db: AsyncSession, id_param: int, id_col: int, id_row: int, update_data: dict) -> Optional[CalibrationValue]:
        item = await db.get(CalibrationValue, (id_param, id_col, id_row))
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        return item

    @staticmethod
    async def delete(db: AsyncSession, id_param: int, id_col: int, id_row: int) -> Optional[CalibrationValue]:
        item = await db.get(CalibrationValue, (id_param, id_col, id_row))
        if item:
            await db.delete(item)
            await db.commit()
        return item