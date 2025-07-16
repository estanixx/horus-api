import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import GCPType, GCPCreateInput, GCPUpdateInput
from app.services import GCPService, StationService
from app.models import GCP

@strawberry.type
class GCPMutation:
    @strawberry.mutation
    async def create_gcp(self, info: Info, input: GCPCreateInput) -> GCPType:
        """Creates a new Ground Control Point (GCP)."""
        db = info.context["db"]
        if not await StationService.get_by_id(db, station_id=input.station_id):
            raise ValueError(f"Station with ID {input.station_id} not found.")
            
        new_item = await GCPService.create(db, GCP(**input.__dict__))
        return GCPType(**new_item.dict())

    @strawberry.mutation
    async def update_gcp(self, info: Info, id: int, input: GCPUpdateInput) -> Optional[GCPType]:
        """Updates an existing GCP by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await GCPService.update(db, gcp_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"GCP with ID {id} not found.")
        return GCPType(**updated_item.dict())

    @strawberry.mutation
    async def delete_gcp(self, info: Info, id: int) -> GCPType:
        """Deletes a GCP by its ID."""
        db = info.context["db"]
        deleted_item = await GCPService.delete(db, gcp_id=id)
        if not deleted_item:
            raise ValueError(f"GCP with ID {id} not found.")
        return GCPType(**deleted_item.dict())