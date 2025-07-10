import strawberry
from typing import List, Optional
from app.graphql.types import ImageType
from app.services.image_service import ImageService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class ImageQuery:

    @strawberry.field
    async def images(self, info) -> List[ImageType]:
        db: AsyncSession = info.context["db"]
        db_images = await ImageService(db).get_all_images()
        return db_images # type: ignore


    @strawberry.field
    async def image(self, info, id: int) -> Optional[ImageType]:
        db: AsyncSession = info.context["db"]
        db_image = await ImageService(db).get_image_by_id(id)
        if not db_image:
            return None
        return db_image # type: ignore