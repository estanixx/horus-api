from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import CameraByFusion

class CameraByFusionService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[CameraByFusion], int]:
        statement = select(CameraByFusion).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(CameraByFusion)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_ids(db: AsyncSession, fusion_id: int, camera_id: int) -> Optional[CameraByFusion]:
        return await db.get(CameraByFusion, (fusion_id, camera_id))

    @staticmethod
    async def get_for_fusion(db: AsyncSession, fusion_id: int, skip: int, limit: int) -> Tuple[List[CameraByFusion], int]:
        statement = select(CameraByFusion).where(CameraByFusion.fusion_id == fusion_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(CameraByFusion).where(CameraByFusion.fusion_id == fusion_id)
        total_count = (await db.exec(count_statement)).one()

        return data, total_count

    @staticmethod
    async def get_for_camera(db: AsyncSession, camera_id: int, skip: int, limit: int) -> Tuple[List[CameraByFusion], int]:
        statement = select(CameraByFusion).where(CameraByFusion.camera_id == camera_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(CameraByFusion).where(CameraByFusion.camera_id == camera_id)
        total_count = (await db.exec(count_statement)).one()

        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: CameraByFusion) -> CameraByFusion:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, fusion_id: int, camera_id: int, update_data: dict) -> Optional[CameraByFusion]:
        item = await db.get(CameraByFusion, (fusion_id, camera_id))
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, fusion_id: int, camera_id: int) -> Optional[CameraByFusion]:
        item = await db.get(CameraByFusion, (fusion_id, camera_id))
        if item:
            await db.delete(item)
            await db.commit()
        return item