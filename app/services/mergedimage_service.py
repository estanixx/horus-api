from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import MergedImage
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from app.graphql.types import MergedImageCreateInput, MergedImageUpdateInput

class MergedImageService:
    
    def __init__(self, db: AsyncSession):
            self.db = db
       
              
    async def get_all_mergedimages(self) -> List[MergedImage]:
        mergedimages = await self.db.exec(select(MergedImage))
        return mergedimages.all()

    @staticmethod
    async def get_mergedimage_by_id(db: AsyncSession, mergedimage_id: int) -> Optional[MergedImage]:

        statement = (
            select(MergedImage)
            .where(MergedImage.id == mergedimage_id)
        )
        result = await db.exec(statement)
        return result.first()


    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[MergedImage], int]:
       
        statement = select(MergedImage).offset(skip).limit(limit)
        result = await db.exec(statement)
        mergedimages = result.all()

        count_statement = select(func.count()).select_from(MergedImage)
        total_count = (await db.exec(count_statement)).one()

        return mergedimages, total_count


    @staticmethod
    async def create(db: AsyncSession, data:  Annotated["MergedImageCreateInput", strawberry.lazy('app.graphql.types')]) -> MergedImage: 
        new_model = MergedImage(**strawberry.asdict(data))
        
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model


    @staticmethod
    async def update(db: AsyncSession, mergedimage_id: int, data:  Annotated["MergedImageUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[MergedImage]:
        mergedImage = await db.get(MergedImage, mergedimage_id)
        if not mergedImage:
            return None

        update_data = strawberry.asdict(data)
        for key, value in update_data.items():
            setattr(mergedImage, key, value)

        db.add(mergedImage)
        await db.commit()
        await db.refresh(mergedImage)
        return mergedImage


    @staticmethod
    async def delete(db: AsyncSession, mergedimage_id: int) -> Optional[MergedImage]:
     
        mergedimage = await db.get(MergedImage, mergedimage_id)
        if not mergedimage:
            return None
        
        await db.delete(mergedimage)
        await db.commit()
        return mergedimage