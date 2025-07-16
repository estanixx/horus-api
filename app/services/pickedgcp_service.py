from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import PickedGCP

class PickedGCPService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[PickedGCP], int]:
        statement = select(PickedGCP).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(PickedGCP)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_ids(db: AsyncSession, calibration_id: int, gcp_id: int) -> Optional[PickedGCP]:
        return await db.get(PickedGCP, (calibration_id, gcp_id))

    @staticmethod
    async def get_for_calibration(db: AsyncSession, calibration_id: int, skip: int, limit: int) -> Tuple[List[PickedGCP], int]:
        statement = select(PickedGCP).where(PickedGCP.calibration_id == calibration_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(PickedGCP).where(PickedGCP.calibration_id == calibration_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_for_gcp(db: AsyncSession, gcp_id: int, skip: int, limit: int) -> Tuple[List[PickedGCP], int]:
        statement = select(PickedGCP).where(PickedGCP.gcp_id == gcp_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(PickedGCP).where(PickedGCP.gcp_id == gcp_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: PickedGCP) -> PickedGCP:
        db.add(data)
        await db.commit()
        # Cannot refresh composite primary key objects yet
        return data

    @staticmethod
    async def update(db: AsyncSession, calibration_id: int, gcp_id: int, update_data: dict) -> Optional[PickedGCP]:
        item = await db.get(PickedGCP, (calibration_id, gcp_id))
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        return item

    @staticmethod
    async def delete(db: AsyncSession, calibration_id: int, gcp_id: int) -> Optional[PickedGCP]:
        item = await db.get(PickedGCP, (calibration_id, gcp_id))
        if item:
            await db.delete(item)
            await db.commit()
        return item