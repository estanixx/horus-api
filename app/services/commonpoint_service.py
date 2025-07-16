from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import CommonPoint

class CommonPointService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[CommonPoint], int]:
        statement = select(CommonPoint).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(CommonPoint)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_ids(db: AsyncSession, id_fusion: int, camera_id: int, name: str) -> Optional[CommonPoint]:
        return await db.get(CommonPoint, (id_fusion, camera_id, name))

    @staticmethod
    async def get_for_fusion(db: AsyncSession, fusion_id: int, skip: int, limit: int) -> Tuple[List[CommonPoint], int]:
        statement = select(CommonPoint).where(CommonPoint.id_fusion == fusion_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(CommonPoint).where(CommonPoint.id_fusion == fusion_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_for_camera(db: AsyncSession, camera_id: int, skip: int, limit: int) -> Tuple[List[CommonPoint], int]:
        statement = select(CommonPoint).where(CommonPoint.camera_id == camera_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(CommonPoint).where(CommonPoint.camera_id == camera_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: CommonPoint) -> CommonPoint:
        db.add(data)
        await db.commit()
        # Cannot refresh composite primary key objects yet
        return data

    @staticmethod
    async def update(db: AsyncSession, id_fusion: int, camera_id: int, name: str, update_data: dict) -> Optional[CommonPoint]:
        item = await db.get(CommonPoint, (id_fusion, camera_id, name))
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        return item

    @staticmethod
    async def delete(db: AsyncSession, id_fusion: int, camera_id: int, name: str) -> Optional[CommonPoint]:
        item = await db.get(CommonPoint, (id_fusion, camera_id, name))
        if item:
            await db.delete(item)
            await db.commit()
        return item