import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import RectifiedImageType, RectifiedImageCreateInput, RectifiedImageUpdateInput
from app.services import RectifiedImageService, CalibrationService, ImageTypeService
from app.models import RectifiedImage

@strawberry.type
class RectifiedImageMutation:
    @strawberry.mutation
    async def create_rectified_image(self, info: Info, input: RectifiedImageCreateInput) -> RectifiedImageType:
        """Creates a new rectified image."""
        db = info.context["db"]
        if input.calibration_id and not await CalibrationService.get_by_id(db, calibration_id=input.calibration_id):
            raise ValueError(f"Calibration with ID {input.calibration_id} not found.")
        if not await ImageTypeService.get_by_id(db, type_id=input.image_type_id):
            raise ValueError(f"ImageType with ID {input.image_type_id} not found.")

        new_item = await RectifiedImageService.create(db, RectifiedImage(**input.__dict__))
        return RectifiedImageType(**new_item.dict())

    @strawberry.mutation
    async def update_rectified_image(self, info: Info, id: int, input: RectifiedImageUpdateInput) -> Optional[RectifiedImageType]:
        """Updates an existing rectified image by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await RectifiedImageService.update(db, image_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"RectifiedImage with ID {id} not found.")
        return RectifiedImageType(**updated_item.dict())

    @strawberry.mutation
    async def delete_rectified_image(self, info: Info, id: int) -> RectifiedImageType:
        """Deletes a rectified image by its ID."""
        db = info.context["db"]
        deleted_item = await RectifiedImageService.delete(db, image_id=id)
        if not deleted_item:
            raise ValueError(f"RectifiedImage with ID {id} not found.")
        return RectifiedImageType(**deleted_item.dict())