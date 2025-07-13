import strawberry
from typing import List, Optional
from app.graphql.types import MergedImageType
from app.services.mergedimage_service import MergedImageService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class MergedImageQuery:

    @strawberry.field
    async def mergedimages(self, info) -> List[MergedImageType]:
        db: AsyncSession = info.context["db"]
        db_mergedimages = await MergedImageService(db).get_all_mergedimages()
        return db_mergedimages # type: ignore


    @strawberry.field
    async def mergedimage(self, info, id: int) -> Optional[MergedImageType]:
        db: AsyncSession = info.context["db"]
        db_mergedimage = await MergedImageService(db).get_mergedimage_by_id(id)
        if not db_mergedimage:
            return None
        return db_mergedimage # type: ignore