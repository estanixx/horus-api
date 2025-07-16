from typing import List, Optional, Tuple, Annotated
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import ImageType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.graphql.types import ImageTypeCreateInput, ImageTypeUpdateInput

class ImageTypeService:

    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[ImageType], int]:
        """Fetches a paginated list of all image types."""
        statement = select(ImageType).offset(skip).limit(limit)
        result = await db.exec(statement)
        image_types = result.all()
        
        count_statement = select(func.count()).select_from(ImageType)
        total_count = (await db.exec(count_statement)).one()
        
        return image_types, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, type_id: int) -> Optional[ImageType]:
        """Fetches an image type by its ID."""
        statement = select(ImageType).where(ImageType.id == type_id)
        result = await db.exec(statement)
        return result.first()
    
    @staticmethod
    async def create(db: AsyncSession, data: Annotated["ImageTypeCreateInput", strawberry.lazy('app.graphql.types')]) -> ImageType:
        """Creates a new image type."""
        new_model = ImageType(**strawberry.asdict(data))
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @staticmethod
    async def update(db: AsyncSession, type_id: int, data: Annotated["ImageTypeUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[ImageType]:
        """Updates an existing image type."""
        image_type = await db.get(ImageType, type_id)
        if not image_type:
            return None

        update_data = strawberry.asdict(data, omit_unset=True)
        for key, value in update_data.items():
            setattr(image_type, key, value)

        db.add(image_type)
        await db.commit()
        await db.refresh(image_type)
        return image_type

    @staticmethod
    async def delete(db: AsyncSession, type_id: int) -> Optional[ImageType]:
        """Deletes an image type."""
        image_type = await db.get(ImageType, type_id)
        if not image_type:
            return None
            
        await db.delete(image_type)
        await db.commit()
        return image_type