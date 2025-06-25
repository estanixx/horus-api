from typing import List, Optional
from sqlmodel import select
from app.models import Station
from sqlmodel.ext.asyncio.session import AsyncSession

class StationService:
    
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all_stations(self) -> List[Station]:
        result = await self.db.exec(select(Station))
        return result.all()


    async def get_station_by_id(self, station_id: int) -> Optional[Station]:
        return await self.db.get(Station, station_id)


    async def get_station_by_alias(self, alias: str) -> Optional[Station]:
        statement = select(Station).where(Station.alias == alias)
        result = await self.db.exec(statement)
        return result.first()


    async def create_station(self, station_create: Station) -> Station:
        self.db.add(station_create)
        await self.db.commit()
        await self.db.refresh(station_create)
        return station_create


    async def update_station(self, station_id: int, station_update: Station) -> Optional[Station]:
        station = await self.db.get(Station, station_id)
        if station:
            update_data = station_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(station, key, value)
            
            self.db.add(station)
            await self.db.commit()
            await self.db.refresh(station)
        return station

    async def delete_station(self, station_id: int) -> bool:
        station = await self.db.get(Station, station_id)
        if station:
            await self.db.delete(station)
            await self.db.commit()
            return True
        return False