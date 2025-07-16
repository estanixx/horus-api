from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import FusionParameter

class FusionParameterService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[FusionParameter], int]:
        statement = select(FusionParameter).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(FusionParameter)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, param_id: int) -> Optional[FusionParameter]:
        return await db.get(FusionParameter, param_id)

    @staticmethod
    async def get_for_fusion(db: AsyncSession, fusion_id: int, skip: int, limit: int) -> Tuple[List[FusionParameter], int]:
        statement = select(FusionParameter).where(FusionParameter.id_fusion == fusion_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(FusionParameter).where(FusionParameter.id_fusion == fusion_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: FusionParameter) -> FusionParameter:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, param_id: int, update_data: dict) -> Optional[FusionParameter]:
        item = await db.get(FusionParameter, param_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, param_id: int) -> Optional[FusionParameter]:
        item = await db.get(FusionParameter, param_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item