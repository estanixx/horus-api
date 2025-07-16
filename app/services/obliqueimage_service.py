from typing import List, Optional, Tuple, Annotated
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import ObliqueImage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.graphql.types import ObliqueImageCreateInput, ObliqueImageUpdateInput

class ObliqueImageService:

    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[ObliqueImage], int]:
        """Fetches a paginated list of all oblique images."""
        statement = select(ObliqueImage).offset(skip).limit(limit)
        result = await db.exec(statement)
        images = result.all()
        
        count_statement = select(func.count()).select_from(ObliqueImage)
        total_count = (await db.exec(count_statement)).one()
        
        return images, total_count

    @staticmethod
    async def get_for_camera(
        db: AsyncSession, camera_id: int, skip: int, limit: int
    ) -> Tuple[List[ObliqueImage], int]:
        """Fetches a paginated list of oblique images for a specific camera."""
        statement = (
            select(ObliqueImage)
            .where(ObliqueImage.camera_id == camera_id)
            .offset(skip)
            .limit(limit)
        )
        result = await db.exec(statement)
        images = result.all()

        count_statement = (
            select(func.count())
            .select_from(ObliqueImage)
            .where(ObliqueImage.camera_id == camera_id)
        )
        total_count = (await db.exec(count_statement)).one()

        return images, total_count
    
    @staticmethod    
    async def get_for_image_type(
        db: AsyncSession, image_type_id: int, skip: int, limit: int
    ) -> Tuple[List[ObliqueImage], int]:
        """Fetches a paginated list of oblique images for a specific camera."""
        statement = (
            select(ObliqueImage)
            .where(ObliqueImage.image_type_id == image_type_id)
            .offset(skip)
            .limit(limit)
        )
        result = await db.exec(statement)
        images = result.all()

        count_statement = (
            select(func.count())
            .select_from(ObliqueImage)
            .where(ObliqueImage.image_type_id == image_type_id)
        )
        total_count = (await db.exec(count_statement)).one()

        return images, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, image_id: int) -> Optional[ObliqueImage]:
        """Fetches an oblique image by its ID."""
        statement = select(ObliqueImage).where(ObliqueImage.id == image_id)
        result = await db.exec(statement)
        return result.first()
    
    @staticmethod
    async def create(db: AsyncSession, data: Annotated["ObliqueImageCreateInput", strawberry.lazy('app.graphql.types')]) -> ObliqueImage:
        """Creates a new oblique image."""
        new_model = ObliqueImage(**strawberry.asdict(data))
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @staticmethod
    async def update(db: AsyncSession, image_id: int, data: Annotated["ObliqueImageUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[ObliqueImage]:
        """Updates an existing oblique image."""
        image = await db.get(ObliqueImage, image_id)
        if not image:
            return None

        update_data = strawberry.asdict(data, omit_unset=True)
        for key, value in update_data.items():
            setattr(image, key, value)

        db.add(image)
        await db.commit()
        await db.refresh(image)
        return image

    @staticmethod
    async def delete(db: AsyncSession, image_id: int) -> Optional[ObliqueImage]:
        """Deletes an oblique image."""
        image = await db.get(ObliqueImage, image_id)
        if not image:
            return None
            
        await db.delete(image)
        await db.commit()
        return image