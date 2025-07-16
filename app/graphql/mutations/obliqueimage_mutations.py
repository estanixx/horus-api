import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ObliqueImageType, ObliqueImageCreateInput, ObliqueImageUpdateInput
from app.services import ObliqueImageService, CameraService, ImageTypeService
from app.models import ObliqueImage

@strawberry.type
class ObliqueImageMutation:
    @strawberry.mutation
    async def create_oblique_image(self, info: Info, input: ObliqueImageCreateInput) -> ObliqueImageType:
        """Creates a new oblique image."""
        db = info.context["db"]
        if not await CameraService.get_by_id(db, camera_id=input.camera_id):
            raise ValueError(f"Camera with ID {input.camera_id} not found.")
        if not await ImageTypeService.get_by_id(db, type_id=input.image_type_id):
            raise ValueError(f"ImageType with ID {input.image_type_id} not found.")
            
        new_item = await ObliqueImageService.create(db, ObliqueImage(**input.__dict__))
        return ObliqueImageType(**new_item.dict())

    @strawberry.mutation
    async def update_oblique_image(self, info: Info, id: int, input: ObliqueImageUpdateInput) -> Optional[ObliqueImageType]:
        """Updates an existing oblique image by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await ObliqueImageService.update(db, image_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"ObliqueImage with ID {id} not found.")
        return ObliqueImageType(**updated_item.dict())

    @strawberry.mutation
    async def delete_oblique_image(self, info: Info, id: int) -> ObliqueImageType:
        """Deletes an oblique image by its ID."""
        db = info.context["db"]
        deleted_item = await ObliqueImageService.delete(db, image_id=id)
        if not deleted_item:
            raise ValueError(f"ObliqueImage with ID {id} not found.")
        return ObliqueImageType(**deleted_item.dict())