# app/graphql/queries/camera_queries.py

"""
GraphQL query resolvers for the Camera model.

Defines queries for fetching cameras, including filtering by station and
providing total counts.
"""

import strawberry
from strawberry.types import Info
from typing import Optional

from app.graphql.types import CameraType, Connection, Edge, PageInfo
from app.services import CameraService, StationService

@strawberry.type
class CameraQuery:
    @strawberry.field
    async def camera(self, info: Info, id: int) -> Optional[CameraType]:
        """Fetches a single camera by its ID."""
        db = info.context["db"]
        camera = await CameraService.get_by_id(db, camera_id=id)
        return CameraType(**camera.dict()) if camera else None

    @strawberry.field
    async def cameras_by_station(
        self, info: Info, station_id: int, skip: int = 0, limit: int = 10
    ) -> Connection[CameraType]:
        """Fetches a paginated list of cameras for a specific station."""
        db = info.context["db"]
        # Optional: Check if station exists
        if not await StationService.get_by_id(db, station_id):
             raise ValueError(f"Station with ID {station_id} not found.")

        cameras, total_count = await CameraService.get_for_station(db, station_id, skip, limit)
        
        edges = [
            Edge(node=CameraType(**camera.dict()), cursor=str(skip + i))
            for i, camera in enumerate(cameras)
        ]

        page_info = PageInfo(
            has_next_page=skip + limit < total_count,
            has_previous_page=skip > 0,
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-1].cursor if edges else None,
        )
        
        return Connection(total_count=total_count, edges=edges, page_info=page_info)

    @strawberry.field
    async def camera_count_by_station(self, info: Info, station_id: int) -> int:
        """Returns the total number of cameras for a specific station."""
        db = info.context["db"]
        _, total_count = await CameraService.get_for_station(db, station_id, 0, 0)
        return total_count

    @strawberry.field
    async def camera_total(self, info: Info) -> int:
        """Returns the total number of cameras across all stations."""
        db = info.context["db"]
        _, total_count = await CameraService.get_all_paginated(db, 0, 0)
        return total_count