# app/services/station_service.py
from typing import List, Optional
from sqlmodel import Session, select
from app.models import Station, Camera # Import models from the __init__.py barrel

# Import AsyncSession for type hinting, as your context will provide an AsyncSession
from sqlmodel.ext.asyncio.session import AsyncSession

class StationService:
    def __init__(self, db: AsyncSession): # Type hint with AsyncSession
        self.db = db

    async def get_all_stations(self) -> List[Station]:
        # Await the execution
        result = await self.db.exec(select(Station))
        return result.all()

    async def get_station_by_id(self, station_id: int) -> Optional[Station]:
        # Await the get operation
        return await self.db.get(Station, station_id)

    async def get_station_by_alias(self, alias: str) -> Optional[Station]:
        # Await the execution
        result = await self.db.exec(select(Station).where(Station.alias == alias))
        return result.first()

    async def create_station(self, station_create: Station) -> Station:
        self.db.add(station_create)
        await self.db.commit() # Await commit
        await self.db.refresh(station_create) # Await refresh
        return station_create

    async def update_station(self, station_id: int, station_update: Station) -> Optional[Station]:
        station = await self.db.get(Station, station_id) # Await get
        if station:
            # Update fields dynamically
            for key, value in station_update.model_dump(exclude_unset=True).items():
                setattr(station, key, value)
            self.db.add(station)
            await self.db.commit() # Await commit
            await self.db.refresh(station) # Await refresh
        return station

    async def delete_station(self, station_id: int) -> bool:
        station = await self.db.get(Station, station_id) # Await get
        if station:
            await self.db.delete(station) # Await delete
            await self.db.commit() # Await commit
            return True
        return False