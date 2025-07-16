from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import RectifiedImage

class RectifiedImageService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[RectifiedImage], int]:
        statement = select(RectifiedImage).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(RectifiedImage)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, image_id: int) -> Optional[RectifiedImage]:
        return await db.get(RectifiedImage, image_id)

    @staticmethod
    async def get_for_calibration(db: AsyncSession, calibration_id: int, skip: int, limit: int) -> Tuple[List[RectifiedImage], int]:
        statement = select(RectifiedImage).where(RectifiedImage.calibration_id == calibration_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(RectifiedImage).where(RectifiedImage.calibration_id == calibration_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: RectifiedImage) -> RectifiedImage:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, image_id: int, update_data: dict) -> Optional[RectifiedImage]:
        item = await db.get(RectifiedImage, image_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, image_id: int) -> Optional[RectifiedImage]:
        item = await db.get(RectifiedImage, image_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item