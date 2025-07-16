from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import ROICoordinate

class ROICoordinateService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[ROICoordinate], int]:
        statement = select(ROICoordinate).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(ROICoordinate)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, coord_id: int) -> Optional[ROICoordinate]:
        # Assuming BaseSQLModel provides a standard 'id' primary key
        return await db.get(ROICoordinate, coord_id)

    @staticmethod
    async def get_for_roi(db: AsyncSession, roi_id: int, skip: int, limit: int) -> Tuple[List[ROICoordinate], int]:
        statement = select(ROICoordinate).where(ROICoordinate.roi_id == roi_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(ROICoordinate).where(ROICoordinate.roi_id == roi_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: ROICoordinate) -> ROICoordinate:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, coord_id: int, update_data: dict) -> Optional[ROICoordinate]:
        item = await db.get(ROICoordinate, coord_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, coord_id: int) -> Optional[ROICoordinate]:
        item = await db.get(ROICoordinate, coord_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item