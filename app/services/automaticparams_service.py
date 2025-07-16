from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import AutomaticParams

class AutomaticParamsService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[AutomaticParams], int]:
        statement = select(AutomaticParams).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(AutomaticParams)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, param_id: int) -> Optional[AutomaticParams]:
        return await db.get(AutomaticParams, param_id)

    @staticmethod
    async def get_for_station(db: AsyncSession, station_id: int, skip: int, limit: int) -> Tuple[List[AutomaticParams], int]:
        statement = select(AutomaticParams).where(AutomaticParams.station_id == station_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(AutomaticParams).where(AutomaticParams.station_id == station_id)
        total_count = (await db.exec(count_statement)).one()

        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: AutomaticParams) -> AutomaticParams:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, param_id: int, update_data: dict) -> Optional[AutomaticParams]:
        param = await db.get(AutomaticParams, param_id)
        if not param:
            return None
        for key, value in update_data.items():
            setattr(param, key, value)
        db.add(param)
        await db.commit()
        await db.refresh(param)
        return param

    @staticmethod
    async def delete(db: AsyncSession, param_id: int) -> Optional[AutomaticParams]:
        param = await db.get(AutomaticParams, param_id)
        if param:
            await db.delete(param)
            await db.commit()
        return param