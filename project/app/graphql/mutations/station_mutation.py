# app/graphql/mutations/station_mutation.py
import strawberry
from typing import Optional
from app.graphql.types import StationType, StationCreateInput, StationUpdateInput # From types barrel
from app.models import Station # Import SQLModel for conversion
from app.services.station_service import StationService
from sqlmodel import Session # For type hinting the db session

@strawberry.type
class StationMutation:
    @strawberry.mutation
    def create_station(self, info, input: StationCreateInput) -> StationType:
        db: Session = info.context["db"]
        station_data = Station.model_validate(input.model_dump())
        return StationService(db).create_station(station_data)

    @strawberry.mutation
    def update_station(self, info, id: int, input: StationUpdateInput) -> Optional[StationType]:
        db: Session = info.context["db"]
        station_data = Station.model_validate(input.model_dump(exclude_unset=True))
        return StationService(db).update_station(id, station_data)

    @strawberry.mutation
    def delete_station(self, info, id: int) -> bool:
        db: Session = info.context["db"]
        return StationService(db).delete_station(id)