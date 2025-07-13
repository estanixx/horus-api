import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MergedImageType, MergedImageCreateInput, MergedImageUpdateInput
from app.services import MergedImageService, ImageService

@strawberry.type
class MergedImageMutation:
    
    @strawberry.mutation
    async def create_mergedimage(self, info: Info, input: MergedImageCreateInput) -> MergedImageType:
        db = info.context["db"]
        if not await ImageService.get_image_by_id(db, input.image_id):
             raise ValueError(f"Image with ID {input.image_id} not found.")
        
        new_mergedimage = await MergedImageService.create(db, data=input)
        return MergedImageType(**new_mergedimage.dict())
    

    @strawberry.mutation
    async def update_mergedimage(
        self, info: Info, id: int, input: MergedImageUpdateInput
    ) -> Optional[MergedImageType]:
        db = info.context["db"]
        updated_mergedimage = await MergedImageService.update(db, mergedimage_id=id, data=input)
        if not updated_mergedimage:
            raise ValueError(f"Rectifiedimage with ID {id} not found.")
        return MergedImageType(**updated_mergedimage.dict())


    @strawberry.mutation
    async def delete_mergedimage(self, info: Info, id: int) -> MergedImageType:
        db = info.context["db"]
        delete_mergedimage = await MergedImageService.delete(db, mergedimage_id=id)
        if not delete_mergedimage:
            raise ValueError(f"Rectifiedimage with ID {id} not found.")
        return MergedImageType(**delete_mergedimage.dict())