from typing import List, Optional, Tuple, Annotated
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import MergedImage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.graphql.types import MergedImageCreateInput, MergedImageUpdateInput

class MergedImageService:

    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[MergedImage], int]:
        """Fetches a paginated list of all merged images."""
        statement = select(MergedImage).offset(skip).limit(limit)
        result = await db.exec(statement)
        images = result.all()
        
        count_statement = select(func.count()).select_from(MergedImage)
        total_count = (await db.exec(count_statement)).one()
        
        return images, total_count

    @staticmethod
    async def get_for_fusion(
        db: AsyncSession, fusion_id: int, skip: int, limit: int
    ) -> Tuple[List[MergedImage], int]:
        """Fetches a paginated list of merged images for a specific fusion."""
        statement = (
            select(MergedImage)
            .where(MergedImage.fusion_id == fusion_id)
            .offset(skip)
            .limit(limit)
        )
        result = await db.exec(statement)
        images = result.all()

        count_statement = (
            select(func.count())
            .select_from(MergedImage)
            .where(MergedImage.fusion_id == fusion_id)
        )
        total_count = (await db.exec(count_statement)).one()

        return images, total_count
        
    @staticmethod
    async def get_for_image_type(
        db: AsyncSession, image_type_id: int, skip: int, limit: int
    ) -> Tuple[List[MergedImage], int]:
        """Fetches a paginated list of merged images for a specific image type."""
        statement = (
            select(MergedImage)
            .where(MergedImage.image_type_id == image_type_id)
            .offset(skip)
            .limit(limit)
        )
        result = await db.exec(statement)
        images = result.all()

        count_statement = (
            select(func.count())
            .select_from(MergedImage)
            .where(MergedImage.image_type_id == image_type_id)
        )
        total_count = (await db.exec(count_statement)).one()

        return images, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, image_id: int) -> Optional[MergedImage]:
        """Fetches a merged image by its ID."""
        statement = select(MergedImage).where(MergedImage.id == image_id)
        result = await db.exec(statement)
        return result.first()
    
    @staticmethod
    async def create(db: AsyncSession, data: Annotated["MergedImageCreateInput", strawberry.lazy('app.graphql.types')]) -> MergedImage:
        """Creates a new merged image."""
        new_model = MergedImage(**strawberry.asdict(data))
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @staticmethod
    async def update(db: AsyncSession, image_id: int, data: Annotated["MergedImageUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[MergedImage]:
        """Updates an existing merged image."""
        image = await db.get(MergedImage, image_id)
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
    async def delete(db: AsyncSession, image_id: int) -> Optional[MergedImage]:
        """Deletes a merged image."""
        image = await db.get(MergedImage, image_id)
        if not image:
            return None
            
        await db.delete(image)
        await db.commit()
        return image
