import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import FusionParameterType, FusionParameterCreateInput, FusionParameterUpdateInput
from app.services import FusionParameterService, FusionService
from app.models import FusionParameter

@strawberry.type
class FusionParameterMutation:
    @strawberry.mutation
    async def create_fusion_parameter(self, info: Info, input: FusionParameterCreateInput) -> FusionParameterType:
        """Creates a new fusion parameter."""
        db = info.context["db"]
        if not await FusionService.get_by_id(db, fusion_id=input.id_fusion):
            raise ValueError(f"Fusion with ID {input.id_fusion} not found.")
            
        new_item = await FusionParameterService.create(db, FusionParameter(**input.__dict__))
        return FusionParameterType(**new_item.dict())

    @strawberry.mutation
    async def update_fusion_parameter(self, info: Info, id: int, input: FusionParameterUpdateInput) -> Optional[FusionParameterType]:
        """Updates an existing fusion parameter by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await FusionParameterService.update(db, param_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"FusionParameter with ID {id} not found.")
        return FusionParameterType(**updated_item.dict())

    @strawberry.mutation
    async def delete_fusion_parameter(self, info: Info, id: int) -> FusionParameterType:
        """Deletes a fusion parameter by its ID."""
        db = info.context["db"]
        deleted_item = await FusionParameterService.delete(db, param_id=id)
        if not deleted_item:
            raise ValueError(f"FusionParameter with ID {id} not found.")
        return FusionParameterType(**deleted_item.dict())