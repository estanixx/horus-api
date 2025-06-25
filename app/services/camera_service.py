from typing import List, Optional
from sqlmodel import select
from app.models import Camera
from sqlmodel.ext.asyncio.session import AsyncSession

class CameraService:

    def __init__(self, db: AsyncSession):
        self.db = db


    async def get_all_cameras(self) -> List[Camera]:
        result = await self.db.exec(select(Camera))
        return result.all()


    async def get_camera_by_id(self, camera_id: int) -> Optional[Camera]:
        return await self.db.get(Camera, camera_id)


    async def create_camera(self, camera_create: Camera) -> Camera:
        self.db.add(camera_create)
        await self.db.commit()
        await self.db.refresh(camera_create)
        return camera_create


    async def update_camera(self, camera_id: int, camera_update: Camera) -> Optional[Camera]:
        camera = await self.db.get(Camera, camera_id)
        if camera:
            update_data = camera_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(camera, key, value)

            self.db.add(camera)
            await self.db.commit()
            await self.db.refresh(camera)
        return camera


    async def delete_camera(self, camera_id: int) -> bool:
        camera = await self.db.get(Camera, camera_id)
        if camera:
            await self.db.delete(camera)
            await self.db.commit()
            return True
        return False
    
    
    async def get_cameras_by_station_id(self, station_id: int) -> List[Camera]:
        statement = select(Camera).where(Camera.station_id == station_id)
        result = await self.db.exec(statement)
        return result.all()