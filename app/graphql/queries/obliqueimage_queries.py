import strawberry
from typing import List, Optional
from app.graphql.types import ObliqueImageType
from app.services.obliqueimage_service import ObliqueImageService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class ObliqueImageQuery:

    @strawberry.field
    async def obliqueimages(self, info) -> List[ObliqueImageType]:
        db: AsyncSession = info.context["db"]
        db_obliqueimages = await ObliqueImageService(db).get_all_obliqueimages
        return db_obliqueimages # type: ignore


    @strawberry.field
    async def obliqueimage(self, info, id: int) -> Optional[ObliqueImageType]:
        db: AsyncSession = info.context["db"]
        db_obliqueimage = await ObliqueImageService(db).get_obliqueimage_by_id(id)
        if not db_obliqueimage:
            return None
        return db_obliqueimage # type: ignore