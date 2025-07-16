from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import CalibrationParameter

class CalibrationParameterService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[CalibrationParameter], int]:
        statement = select(CalibrationParameter).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(CalibrationParameter)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, param_id: int) -> Optional[CalibrationParameter]:
        return await db.get(CalibrationParameter, param_id)

    @staticmethod
    async def get_for_calibration(db: AsyncSession, calibration_id: int, skip: int, limit: int) -> Tuple[List[CalibrationParameter], int]:
        statement = select(CalibrationParameter).where(CalibrationParameter.calibration_id == calibration_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(CalibrationParameter).where(CalibrationParameter.calibration_id == calibration_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: CalibrationParameter) -> CalibrationParameter:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, param_id: int, update_data: dict) -> Optional[CalibrationParameter]:
        item = await db.get(CalibrationParameter, param_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, param_id: int) -> Optional[CalibrationParameter]:
        item = await db.get(CalibrationParameter, param_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item