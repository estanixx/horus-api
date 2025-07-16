from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
from app.models import GCP

class GCPService:
    @staticmethod
    async def get_all_paginated(db: AsyncSession, skip: int, limit: int) -> Tuple[List[GCP], int]:
        statement = select(GCP).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()
        
        count_statement = select(func.count()).select_from(GCP)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, gcp_id: int) -> Optional[GCP]:
        return await db.get(GCP, gcp_id)

    @staticmethod
    async def get_for_station(db: AsyncSession, station_id: int, skip: int, limit: int) -> Tuple[List[GCP], int]:
        statement = select(GCP).where(GCP.station_id == station_id).offset(skip).limit(limit)
        result = await db.exec(statement)
        data = result.all()

        count_statement = select(func.count()).select_from(GCP).where(GCP.station_id == station_id)
        total_count = (await db.exec(count_statement)).one()
        
        return data, total_count

    @staticmethod
    async def create(db: AsyncSession, data: GCP) -> GCP:
        db.add(data)
        await db.commit()
        await db.refresh(data)
        return data

    @staticmethod
    async def update(db: AsyncSession, gcp_id: int, update_data: dict) -> Optional[GCP]:
        item = await db.get(GCP, gcp_id)
        if not item:
            return None
        for key, value in update_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item

    @staticmethod
    async def delete(db: AsyncSession, gcp_id: int) -> Optional[GCP]:
        item = await db.get(GCP, gcp_id)
        if item:
            await db.delete(item)
            await db.commit()
        return item