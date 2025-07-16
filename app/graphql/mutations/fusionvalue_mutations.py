import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import FusionValueType, FusionValueCreateInput, FusionValueUpdateInput
from app.services import FusionValueService, FusionParameterService
from app.models import FusionValue

@strawberry.type
class FusionValueMutation:
    @strawberry.mutation
    async def create_fusion_value(self, info: Info, input: FusionValueCreateInput) -> FusionValueType:
        """Creates a new fusion value."""
        db = info.context["db"]
        if not await FusionParameterService.get_by_id(db, param_id=input.matrix_id):
            raise ValueError(f"FusionParameter with ID {input.matrix_id} not found.")
            
        new_item = await FusionValueService.create(db, FusionValue(**input.__dict__))
        return FusionValueType(**new_item.dict())

    @strawberry.mutation
    async def update_fusion_value(self, info: Info, matrix_id: int, id_col: int, id_row: int, input: FusionValueUpdateInput) -> Optional[FusionValueType]:
        """Updates an existing fusion value by its composite ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await FusionValueService.update(db, matrix_id=matrix_id, id_col=id_col, id_row=id_row, update_data=update_data)
        if not updated_item:
            raise ValueError(f"FusionValue with ID ({matrix_id}, {id_col}, {id_row}) not found.")
        return FusionValueType(**updated_item.dict())

    @strawberry.mutation
    async def delete_fusion_value(self, info: Info, matrix_id: int, id_col: int, id_row: int) -> FusionValueType:
        """Deletes a fusion value by its composite ID."""
        db = info.context["db"]
        deleted_item = await FusionValueService.delete(db, matrix_id=matrix_id, id_col=id_col, id_row=id_row)
        if not deleted_item:
            raise ValueError(f"FusionValue with ID ({matrix_id}, {id_col}, {id_row}) not found.")
        return FusionValueType(**deleted_item.dict())