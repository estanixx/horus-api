from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import Calibration

class CalibrationService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[Calibration], int]:
        statement = select(Calibration).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(Calibration)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, calibration_id: int) -> Optional[Calibration]:
        return await db.get(Calibration, calibration_id)

    @staticmethod
    async def get_for_camera(db: AsyncSession, camera_id: int, skip: int, limit: int) -> Tuple[List[Calibration], int]:
        statement = select(Calibration).where(Calibration.camera_id == camera_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(Calibration).where(Calibration.camera_id == camera_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: Calibration) -> Calibration:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, calibration_id: int, update_data: dict) -> Optional[Calibration]:
        item = await db.get(Calibration, calibration_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, calibration_id: int) -> Optional[Calibration]:
        item = await db.get(Calibration, calibration_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item