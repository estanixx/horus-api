# app/graphql/queries/station_query.py
import strawberry
from typing import List, Optional
from app.graphql.types import StationType # Import from the types barrel
from app.services.station_service import StationService
from sqlmodel import Session # For type hinting the db session

@strawberry.type
class StationQuery:
    @strawberry.field
    def stations(self, info) -> List[StationType]:
        db: Session = info.context["db"]
        return StationService(db).get_all_stations()

    @strawberry.field
    def station(self, info, id: int) -> Optional[StationType]:
        db: Session = info.context["db"]
        return StationService(db).get_station_by_id(id)