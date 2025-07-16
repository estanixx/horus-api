import strawberry
from strawberry.types import Info
from typing import Optional
from app.graphql.types import AutomaticParamsType, AutomaticParamsCreateInput, AutomaticParamsUpdateInput
from app.services import AutomaticParamsService, StationService
from app.models import AutomaticParams

@strawberry.type
class AutomaticParamsMutation:
    @strawberry.mutation
    async def create_automatic_param(self, info: Info, input: AutomaticParamsCreateInput) -> AutomaticParamsType:
        """Creates new automatic parameters for a station."""
        db = info.context["db"]
        if not await StationService.get_by_id(db, station_id=input.station_id):
            raise ValueError(f"Station with ID {input.station_id} not found.")
            
        new_item = await AutomaticParamsService.create(db, AutomaticParams(**input.__dict__))
        return AutomaticParamsType(**new_item.dict())

    @strawberry.mutation
    async def update_automatic_param(self, info: Info, id: int, input: AutomaticParamsUpdateInput) -> Optional[AutomaticParamsType]:
        """Updates existing automatic parameters by its ID."""
        db = info.context["db"]
        update_data = {k: v for k, v in input.__dict__.items() if v is not None}
        updated_item = await AutomaticParamsService.update(db, param_id=id, update_data=update_data)
        if not updated_item:
            raise ValueError(f"AutomaticParams with ID {id} not found.")
        return AutomaticParamsType(**updated_item.dict())

    @strawberry.mutation
    async def delete_automatic_param(self, info: Info, id: int) -> AutomaticParamsType:
        """Deletes automatic parameters by its ID."""
        db = info.context["db"]
        deleted_item = await AutomaticParamsService.delete(db, param_id=id)
        if not deleted_item:
            raise ValueError(f"AutomaticParams with ID {id} not found.")
        return AutomaticParamsType(**deleted_item.dict())