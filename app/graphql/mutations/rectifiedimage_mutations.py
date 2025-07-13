import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import RectifiedImageType, RectifiedImageCreateInput, RectifiedImageUpdateInput
from app.services import RectifiedImageService, ImageService

@strawberry.type
class RectifiedImageMutation:
    
    @strawberry.mutation
    async def create_rectifiedimage(self, info: Info, input: RectifiedImageCreateInput) -> RectifiedImageType:
        db = info.context["db"]
        if not await ImageService.get_image_by_id(db, input.image_id):
             raise ValueError(f"Image with ID {input.image_id} not found.")
        
        new_rectifiedimage = await RectifiedImageService.create(db, data=input)
        return RectifiedImageType(**new_rectifiedimage.dict())
    

    @strawberry.mutation
    async def update_rectifiedimage(
        self, info: Info, id: int, input: RectifiedImageUpdateInput
    ) -> Optional[RectifiedImageType]:
        db = info.context["db"]
        updated_rectifiedimage = await RectifiedImageService.update(db, rectifiedimage_id=id, data=input)
        if not updated_rectifiedimage:
            raise ValueError(f"Rectifiedimage with ID {id} not found.")
        return RectifiedImageType(**updated_rectifiedimage.dict())


    @strawberry.mutation
    async def delete_rectifiedimage(self, info: Info, id: int) -> RectifiedImageType:
        db = info.context["db"]
        deleted_rectifiedimage = await RectifiedImageService.delete(db, rectifiedimage_id=id)
        if not deleted_rectifiedimage:
            raise ValueError(f"Rectifiedimage with ID {id} not found.")
        return RectifiedImageType(**deleted_rectifiedimage.dict())