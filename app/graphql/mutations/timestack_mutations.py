import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import TimeStackType, TimeStackCreateInput, TimeStackUpdateInput
from app.services import TimeStackService, CameraService
from app.models import TimeStack

@strawberry.type
class TimeStackMutation:
    @strawberry.mutation
    async def create_time_stack(self, info: Info, input: TimeStackCreateInput) -> TimeStackType:
        """Creates a new timestack."""
        db = info.context["db"]
        if input.camera_id and not await CameraService.get_by_id(db, camera_id=input.camera_id):
            raise ValueError(f"Camera with ID {input.camera_id} not found.")
            
        new_item = await TimeStackService.create(db, TimeStack(**input.__dict__))
        return TimeStackType(**new_item.dict())

    @strawberry.mutation
    async def update_time_stack(self, info: Info, filename: str, input: TimeStackUpdateInput) -> Optional[TimeStackType]:
        """Updates an existing timestack by its filename."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await TimeStackService.update(db, filename=filename, update_data=update_data)
        if not updated_item:
            raise ValueError(f"TimeStack with filename {filename} not found.")
        return TimeStackType(**updated_item.dict())

    @strawberry.mutation
    async def delete_time_stack(self, info: Info, filename: str) -> TimeStackType:
        """Deletes a timestack by its filename."""
        db = info.context["db"]
        deleted_item = await TimeStackService.delete(db, filename=filename)
        if not deleted_item:
            raise ValueError(f"TimeStack with filename {filename} not found.")
        return TimeStackType(**deleted_item.dict())