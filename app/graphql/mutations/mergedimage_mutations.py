import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import MergedImageType, MergedImageCreateInput, MergedImageUpdateInput
from app.services import MergedImageService, FusionService, ImageTypeService
from app.models import MergedImage

@strawberry.type
class MergedImageMutation:
    @strawberry.mutation
    async def create_merged_image(self, info: Info, input: MergedImageCreateInput) -> MergedImageType:
        """Creates a new merged image."""
        db = info.context["db"]
        if not await FusionService.get_by_id(db, fusion_id=input.fusion_id):
            raise ValueError(f"Fusion with ID {input.fusion_id} not found.")
        if not await ImageTypeService.get_by_id(db, type_id=input.image_type_id):
            raise ValueError(f"ImageType with ID {input.image_type_id} not found.")
            
        new_item = await MergedImageService.create(db, MergedImage(**input.__dict__))
        return MergedImageType(**new_item.dict())

    @strawberry.mutation
    async def update_merged_image(self, info: Info, id: int, input: MergedImageUpdateInput) -> Optional[MergedImageType]:
        """Updates an existing merged image by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await MergedImageService.update(db, image_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"MergedImage with ID {id} not found.")
        return MergedImageType(**updated_item.dict())

    @strawberry.mutation
    async def delete_merged_image(self, info: Info, id: int) -> MergedImageType:
        """Deletes a merged image by its ID."""
        db = info.context["db"]
        deleted_item = await MergedImageService.delete(db, image_id=id)
        if not deleted_item:
            raise ValueError(f"MergedImage with ID {id} not found.")
        return MergedImageType(**deleted_item.dict())
