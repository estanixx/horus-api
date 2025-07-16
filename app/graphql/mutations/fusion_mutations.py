import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import FusionType, FusionCreateInput, FusionUpdateInput
from app.services import FusionService
from app.models import Fusion

@strawberry.type
class FusionMutation:
    @strawberry.mutation
    async def create_fusion(self, info: Info, input: FusionCreateInput) -> FusionType:
        """Creates a new fusion."""
        db = info.context["db"]
        new_item = await FusionService.create(db, Fusion(**input.__dict__))
        return FusionType(**new_item.dict())

    @strawberry.mutation
    async def update_fusion(self, info: Info, id: int, input: FusionUpdateInput) -> Optional[FusionType]:
        """Updates an existing fusion by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await FusionService.update(db, fusion_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"Fusion with ID {id} not found.")
        return FusionType(**updated_item.dict())

    @strawberry.mutation
    async def delete_fusion(self, info: Info, id: int) -> FusionType:
        """Deletes a fusion by its ID."""
        db = info.context["db"]
        deleted_item = await FusionService.delete(db, fusion_id=id)
        if not deleted_item:
            raise ValueError(f"Fusion with ID {id} not found.")
        return FusionType(**deleted_item.dict())