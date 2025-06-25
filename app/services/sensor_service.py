from typing import List, Optional
from sqlmodel import select
from app.models import Sensor
from sqlmodel.ext.asyncio.session import AsyncSession

class SensorService:

    def __init__(self, db: AsyncSession):
            self.db = db
       
               
    async def get_all_sensors(self) -> List[Sensor]:
        result = await self.db.exec(select(Sensor))
        return result.all()
    
    
    async def get_sensor_by_id(self, sensor_id: int) -> Optional[Sensor]:
        return await self.db.get(Sensor, sensor_id)
    
    
    async def save_sensor(self, new_sensor: Sensor) -> Sensor:
        self.db.add(new_sensor)
        await self.db.commit()
        await self.db.refresh(new_sensor)
        return new_sensor
    
    
    async def update_sensor(self, sensor_id: int, sensor_update: Sensor) -> Optional[Sensor]:
        sensor = await self.db.get(Sensor, sensor_id)
        if sensor:
            update_data = sensor_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(sensor, key, value)

            self.db.add(sensor)
            await self.db.commit()
            await self.db.refresh(sensor)
        return sensor
    
    
    async def delete_sensor(self, sensor_id: int) -> bool:
        sensor = await self.db.get(Sensor, sensor_id)
        if sensor:
            await self.db.delete(sensor)
            await self.db.commit()
            return True
        return False
    
    
    async def get_sensors_by_station_id(self, station_id: int) -> List[Sensor]:
        statement = select(Sensor).where(Sensor.station_id == station_id)
        result = await self.db.exec(statement)
        return result.all()
        