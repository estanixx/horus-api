import strawberry
from strawberry.types import Info
from typing import Optional

from app.graphql.types import SensorType, Connection, Edge, PageInfo
from app.services import SensorService, StationService

@strawberry.type
class SensorQuery:
    @strawberry.field
    async def sensor(self, info: Info, id: int) -> Optional[SensorType]:
        """Fetches a single sensor by its ID."""
        db = info.context["db"]
        sensor = await SensorService.get_by_id(db, sensor_id=id)
        return SensorType(**sensor.dict()) if sensor else None

    @strawberry.field
    async def sensors_by_station(
        self, info: Info, station_id: int, skip: int = 0, limit: int = 10
    ) -> Connection[SensorType]:
        """Fetches a paginated list of sensors for a specific station."""
        db = info.context["db"]
        # Optional: Check if station exists
        if not await StationService.get_by_id(db, station_id):
             raise ValueError(f"Station with ID {station_id} not found.")

        sensors, total_count = await SensorService.get_for_station(db, station_id, skip, limit)
        
        edges = [
            Edge(node=SensorType(**sensor.dict()), cursor=str(skip + i))
            for i, sensor in enumerate(sensors)
        ]

        page_info = PageInfo(
            has_next_page=skip + limit < total_count,
            has_previous_page=skip > 0,
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-1].cursor if edges else None,
        )
        
        return Connection(total_count=total_count, edges=edges, page_info=page_info)

    @strawberry.field
    async def sensor_count_by_station(self, info: Info, station_id: int) -> int:
        """Returns the total number of sensors for a specific station."""
        db = info.context["db"]
        _, total_count = await SensorService.get_for_station(db, station_id, 0, 0)
        return total_count

    @strawberry.field
    async def sensor_total(self, info: Info) -> int:
        """Returns the total number of sensors across all stations."""
        db = info.context["db"]
        _, total_count = await SensorService.get_all_paginated(db, 0, 0)
        return total_count