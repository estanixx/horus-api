import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ObliqueImageType, ObliqueImageCreateInput, ObliqueImageUpdateInput
from app.services import ObliqueImageService

@strawberry.type
class ObliqueImageMutation:
    @strawberry.mutation
    async def create_obliqueimage(self, info: Info, input: ObliqueImageCreateInput) -> SensorType:
        db = info.context["db"]
        new_obliqueimage = await ObliqueImageService.create(db, data=input)
        return ObliqueImageType(**new_obliqueimage.dict())

    @strawberry.mutation
    async def update_obliqueimage(
        self, info: Info, id: int, input: ObliqueImageUpdateInput
    ) -> Optional[ObliqueImageType]:
        db = info.context["db"]
        updated_obliqueimage = await ObliqueImageService.update(db, obliqueimage_id=id, data=input)
        if not updated_obliqueimage:
            raise ValueError(f"Obliqueimage with ID {id} not found.")
        return ObliqueImageType(**updated_obliqueimage.dict())

    @strawberry.mutation
    async def delete_obliqueimage(self, info: Info, id: int) -> ObliqueImageType:
        db = info.context["db"]
        deleted_obliqueimage = await ObliqueImageService.delete(db, obliqueimage_id=id)
        if not deleted_obliqueimage:
            raise ValueError(f"Obliqueimage with ID {id} not found.")
        return ObliqueImageType(**deleted_obliqueimage.dict())