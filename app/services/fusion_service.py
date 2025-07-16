from typing import List, Optional, Tuple, Annotated
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy import func
import strawberry
from app.models import Fusion
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.graphql.types import FusionCreateInput, FusionUpdateInput

class FusionService:

    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[Fusion], int]:
        """Fetches a paginated list of all fusions."""
        statement = select(Fusion).offset(skip).limit(limit)
        result = await db.exec(statement)
        fusions = result.all()
        
        count_statement = select(func.count()).select_from(Fusion)
        total_count = (await db.exec(count_statement)).one()
        
        return fusions, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, fusion_id: int) -> Optional[Fusion]:
        """Fetches a fusion by its ID."""
        statement = select(Fusion).where(Fusion.id == fusion_id)
        result = await db.exec(statement)
        return result.first()
    
    @staticmethod
    async def create(db: AsyncSession, data: Annotated["FusionCreateInput", strawberry.lazy('app.graphql.types')]) -> Fusion:
        """Creates a new fusion."""
        new_model = Fusion(**strawberry.asdict(data))
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @staticmethod
    async def update(db: AsyncSession, fusion_id: int, data: Annotated["FusionUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[Fusion]:
        """Updates an existing fusion."""
        fusion = await db.get(Fusion, fusion_id)
        if not fusion:
            return None

        update_data = strawberry.asdict(data, omit_unset=True)
        for key, value in update_data.items():
            setattr(fusion, key, value)

        db.add(fusion)
        await db.commit()
        await db.refresh(fusion)
        return fusion

    @staticmethod
    async def delete(db: AsyncSession, fusion_id: int) -> Optional[Fusion]:
        """Deletes a fusion."""
        fusion = await db.get(Fusion, fusion_id)
        if not fusion:
            return None
            
        await db.delete(fusion)
        await db.commit()
        return fusion