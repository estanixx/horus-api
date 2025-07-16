from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import TimeStack

class TimeStackService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[TimeStack], int]:
        statement = select(TimeStack).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(TimeStack)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, filename: str) -> Optional[TimeStack]:
        return await db.get(TimeStack, filename)

    @staticmethod
    async def get_for_camera(db: AsyncSession, camera_id: int, skip: int, limit: int) -> Tuple[List[TimeStack], int]:
        statement = select(TimeStack).where(TimeStack.camera_id == camera_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(TimeStack).where(TimeStack.camera_id == camera_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: TimeStack) -> TimeStack:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, filename: str, update_data: dict) -> Optional[TimeStack]:
        item = await db.get(TimeStack, filename)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, filename: str) -> Optional[TimeStack]:
        item = await db.get(TimeStack, filename)
        if item:
            await db.delete(item)
            await db.commit()
        return item