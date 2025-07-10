from typing import List, Optional
from sqlmodel import select
from app.models import Image
from sqlmodel.ext.asyncio.session import AsyncSession

class ImageService:
    
    def __init__(self, db: AsyncSession):
            self.db = db
       
               
    async def get_all_images(self) -> List[Image]:
        images = await self.db.exec(select(Image))
        return images.all()
    
    
    async def get_image_by_id(self, image_id: int) -> Optional[Image]:
        return await self.db.get(Image, image_id)
    
    
    async def save_image(self, new_image: Image) -> Image:
        self.db.add(new_image)
        await self.db.commit()
        await self.db.refresh(new_image)
        return new_image
    
    
    async def update_image(self, image_id: int, image_update: Image) -> Optional[Image]:
        image = await self.db.get(Image, image_id)
        if image:
            update_data = image_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(image, key, value)

            self.db.add(image)
            await self.db.commit()
            await self.db.refresh(image)
        return image
    
    
    async def delete_image(self, image_id: int) -> bool:
        image = await self.db.get(Image, image_id)
        if image:
            await self.db.delete(image)
            await self.db.commit()
            return True
        return image
    