from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import RectifiedImage
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from app.graphql.types import RectifiedImageCreateInput, RectifiedImageUpdateInput

class RectifiedImageService:

    @staticmethod
    async def get_rectifiedimage_by_id(db: AsyncSession, rectifiedimage_id: int) -> Optional[RectifiedImage]:

        statement = (
            select(RectifiedImage)
            .where(RectifiedImage.id == rectifiedimage_id)
        )
        result = await db.exec(statement)
        return result.first()


    @staticmethod
    async def get_rectifiedimages_for_image(
        db: AsyncSession, image_id: int, skip: int, limit: int
    ) -> Tuple[List[RectifiedImage], int]:
        statement = (
            select(RectifiedImage)
            .where(RectifiedImage.image_id == image_id)
            .offset(skip)
            .limit(limit)
        )
        result = await db.exec(statement)
        rectifiedimages = result.all()
        
        count_statement = select(func.count()).select_from(RectifiedImage).where(RectifiedImage.image_id == image_id)
        total_count = (await db.exec(count_statement)).one()
        
        return rectifiedimages, total_count


    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[RectifiedImage], int]:
       
        statement = select(RectifiedImage).offset(skip).limit(limit)
        result = await db.exec(statement)
        rectifiedimages = result.all()

        count_statement = select(func.count()).select_from(RectifiedImage)
        total_count = (await db.exec(count_statement)).one()

        return rectifiedimages, total_count


    @staticmethod
    async def create(db: AsyncSession, data:  Annotated["RectifiedImageCreateInput", strawberry.lazy('app.graphql.types')]) -> RectifiedImage: 
        new_model = RectifiedImage(**strawberry.asdict(data))
        
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model


    @staticmethod
    async def update(db: AsyncSession, rectifiedimage_id: int, data:  Annotated["RectifiedImageUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[RectifiedImage]:
        rectifiedImage = await db.get(RectifiedImage, rectifiedimage_id)
        if not rectifiedImage:
            return None

        update_data = strawberry.asdict(data)
        for key, value in update_data.items():
            setattr(rectifiedImage, key, value)

        db.add(rectifiedImage)
        await db.commit()
        await db.refresh(rectifiedImage)
        return rectifiedImage


    @staticmethod
    async def delete(db: AsyncSession, rectifiedimage_id: int) -> Optional[RectifiedImage]:
     
        rectifiedimage = await db.get(RectifiedImage, rectifiedimage_id)
        if not rectifiedimage:
            return None
        
        await db.delete(rectifiedimage)
        await db.commit()
        return rectifiedimage