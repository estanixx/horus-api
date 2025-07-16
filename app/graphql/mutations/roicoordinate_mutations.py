import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import ROICoordinateType, ROICoordinateCreateInput, ROICoordinateUpdateInput
from app.services import ROICoordinateService, ROIService
from app.models import ROICoordinate

@strawberry.type
class ROICoordinateMutation:
    @strawberry.mutation
    async def create_roi_coordinate(self, info: Info, input: ROICoordinateCreateInput) -> ROICoordinateType:
        """Creates a new ROI coordinate."""
        db = info.context["db"]
        if not await ROIService.get_by_id(db, roi_id=input.roi_id):
            raise ValueError(f"ROI with ID {input.roi_id} not found.")
            
        new_item = await ROICoordinateService.create(db, ROICoordinate(**input.__dict__))
        return ROICoordinateType(**new_item.dict())

    @strawberry.mutation
    async def update_roi_coordinate(self, info: Info, id: int, input: ROICoordinateUpdateInput) -> Optional[ROICoordinateType]:
        """Updates an existing ROI coordinate by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await ROICoordinateService.update(db, coord_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"ROICoordinate with ID {id} not found.")
        return ROICoordinateType(**updated_item.dict())

    @strawberry.mutation
    async def delete_roi_coordinate(self, info: Info, id: int) -> ROICoordinateType:
        """Deletes an ROI coordinate by its ID."""
        db = info.context["db"]
        deleted_item = await ROICoordinateService.delete(db, coord_id=id)
        if not deleted_item:
            raise ValueError(f"ROICoordinate with ID {id} not found.")
        return ROICoordinateType(**deleted_item.dict())