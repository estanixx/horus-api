from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import FusionValue

class FusionValueService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[FusionValue], int]:
        statement = select(FusionValue).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(FusionValue)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_ids(db: AsyncSession, matrix_id: int, id_col: int, id_row: int) -> Optional[FusionValue]:
        return await db.get(FusionValue, (matrix_id, id_col, id_row))

    @staticmethod
    async def get_for_parameter(db: AsyncSession, matrix_id: int, skip: int, limit: int) -> Tuple[List[FusionValue], int]:
        statement = select(FusionValue).where(FusionValue.matrix_id == matrix_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(FusionValue).where(FusionValue.matrix_id == matrix_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: FusionValue) -> FusionValue:
        db.add(data)
        await db.commit()
        # Cannot refresh composite primary key objects yet
        return data

    @staticmethod
    async def update(db: AsyncSession, matrix_id: int, id_col: int, id_row: int, update_data: dict) -> Optional[FusionValue]:
        item = await db.get(FusionValue, (matrix_id, id_col, id_row))
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        return item

    @staticmethod
    async def delete(db: AsyncSession, matrix_id: int, id_col: int, id_row: int) -> Optional[FusionValue]:
        item = await db.get(FusionValue, (matrix_id, id_col, id_row))
        if item:
            await db.delete(item)
            await db.commit()
        return item