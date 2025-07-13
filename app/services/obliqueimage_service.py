from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import Obliqueimage
from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from app.graphql.types import ObliqueImageCreateInput, ObliqueImageUpdateInput

class ObliqueImageService:
    
    def __init__(self, db: AsyncSession):
            self.db = db
       
              
    async def get_all_obliqueimages(self) -> List[Obliqueimage]:
        obliqueimages = await self.db.exec(select(Obliqueimage))
        return obliqueimages.all()
    
    
    async def get_obliqueimage_by_id(self, obliqueimage_id: int) -> Optional[Obliqueimage]:
        return await self.db.get(Obliqueimage, obliqueimage_id)
    
    
    @staticmethod
    async def get_by_id(db: AsyncSession, obliqueimage_id: int) -> Optional[Obliqueimage]:
       
        statement = (
            select(Obliqueimage)
            .where(Obliqueimage.id == obliqueimage_id)
        )
        result = await db.exec(statement)
        return result.first()


    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[Obliqueimage], int]:
        
        statement = select(Obliqueimage).offset(skip).limit(limit)
        result = await db.exec(statement)
        obliqueimage = result.all()

        count_statement = select(func.count()).select_from(Obliqueimage)
        total_count = (await db.exec(count_statement)).one()

        return obliqueimage, total_count


    @staticmethod
    async def create(db: AsyncSession, data:  Annotated["ObliqueImageCreateInput", strawberry.lazy('app.graphql.types')]) -> Obliqueimage: 
        new_model = Obliqueimage(**strawberry.asdict(data))
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model


    @staticmethod
    async def update(db: AsyncSession, obliqueimage_id: int, data:  Annotated["ObliqueImageUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[Obliqueimage]:
        obliqueimage = await db.get(Obliqueimage, obliqueimage_id)
        if not obliqueimage:
            return None

        update_data = strawberry.asdict(data)
        for key, value in update_data.items():
            setattr(obliqueimage, key, value)

        db.add(obliqueimage)
        await db.commit()
        await db.refresh(obliqueimage)
        return obliqueimage


    @staticmethod
    async def delete(db: AsyncSession, obliqueimage_id: int) -> Optional[Obliqueimage]:
        obliqueimage = await db.get(Obliqueimage, obliqueimage_id)
        if not obliqueimage:
            return None
        
        await db.delete(obliqueimage)
        await db.commit()
        return obliqueimage