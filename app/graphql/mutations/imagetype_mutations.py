import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ImageTypeType, ImageTypeCreateInput, ImageTypeUpdateInput
from app.services import ImageTypeService
from app.models import ImageType

@strawberry.type
class ImageTypeMutation:
    @strawberry.mutation
    async def create_image_type(self, info: Info, input: ImageTypeCreateInput) -> ImageTypeType:
        """Creates a new image type."""
        db = info.context["db"]
        new_item = await ImageTypeService.create(db, ImageType(**input.__dict__))
        return ImageTypeType(**new_item.dict())

    @strawberry.mutation
    async def update_image_type(self, info: Info, id: int, input: ImageTypeUpdateInput) -> Optional[ImageTypeType]:
        """Updates an existing image type by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await ImageTypeService.update(db, type_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"ImageType with ID {id} not found.")
        return ImageTypeType(**updated_item.dict())

    @strawberry.mutation
    async def delete_image_type(self, info: Info, id: int) -> ImageTypeType:
        """Deletes an image type by its ID."""
        db = info.context["db"]
        deleted_item = await ImageTypeService.delete(db, type_id=id)
        if not deleted_item:
            raise ValueError(f"ImageType with ID {id} not found.")
        return ImageTypeType(**deleted_item.dict())