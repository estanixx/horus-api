import strawberry
from typing import Optional
from app.graphql.types import ImageType, ImageCreateInput, ImageUpdateInput
from app.models import Image
from app.services import ImageService
from sqlmodel.ext.asyncio.session import AsyncSession


@strawberry.type
class ImageMutation:
    
    @strawberry.mutation
    async def create_image(self, info, input: ImageCreateInput) -> ImageType:
        db: AsyncSession = info.context["db"]
        input_dict = strawberry.asdict(input)
        data = Image.parse_obj(input_dict)
        image = await ImageService(db).save_image(data)
        return image  # type: ignore

    @strawberry.mutation
    async def update_image(
        self, info, id: int, input: ImageUpdateInput
    ) -> Optional[ImageType]:
        db: AsyncSession = info.context["db"]
        input_dict = {
            k: v for k, v in strawberry.asdict(input).items() if v is not None
        }
        data = Image.parse_obj(input_dict)
        image = await ImageService(db).update_image(id, data)
        return image  # type: ignore

    @strawberry.mutation
    async def delete_image(self, info, id: int) -> bool:
        db: AsyncSession = info.context["db"]
        deleted = await ImageService(db).delete_image(id)
        return deleted
