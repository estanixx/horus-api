# app/services/camera_service.py
from typing import List, Optional
from sqlmodel import Session, select
from app.models import Camera, Station # Import models from the __init__.py barrel

# Import AsyncSession for type hinting, as your context will provide an AsyncSession
from sqlmodel.ext.asyncio.session import AsyncSession

class CameraService:
    def __init__(self, db: AsyncSession): # Type hint with AsyncSession
        self.db = db

    async def get_all_cameras(self) -> List[Camera]:
        # Await the execution
        result = await self.db.exec(select(Camera))
        return result.all()

    async def get_camera_by_id(self, camera_id: int) -> Optional[Camera]:
        # Await the get operation
        return await self.db.get(Camera, camera_id)

    async def create_camera(self, camera_create: Camera) -> Camera:
        self.db.add(camera_create)
        await self.db.commit() # Await commit
        await self.db.refresh(camera_create) # Await refresh
        return camera_create

    async def update_camera(self, camera_id: int, camera_update: Camera) -> Optional[Camera]:
        camera = await self.db.get(Camera, camera_id) # Await get
        if camera:
            for key, value in camera_update.model_dump(exclude_unset=True).items():
                setattr(camera, key, value)
            self.db.add(camera)
            await self.db.commit() # Await commit
            await self.db.refresh(camera) # Await refresh
        return camera

    async def delete_camera(self, camera_id: int) -> bool:
        camera = await self.db.get(Camera, camera_id) # Await get
        if camera:
            await self.db.delete(camera) # Await delete
            await self.db.commit() # Await commit
            return True
        return False
    
    async def get_cameras_by_station_id(self, station_id: int) -> List[Camera]:
        # Await the execution
        result = await self.db.exec(select(Camera).where(Camera.station_id == station_id))
        return result.all()