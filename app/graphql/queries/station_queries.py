# app/graphql/queries/station_queries.py

"""
GraphQL query resolvers for the Station model.

This module defines the query fields for retrieving station data, such as
fetching a single station by its ID or querying a paginated list of all
stations.
"""

import strawberry
from strawberry.types import Info
from typing import Optional

from app.graphql.types import StationType, Connection, Edge, PageInfo
from app.services import StationService

@strawberry.type
class StationQuery:
    @strawberry.field
    async def station(self, info: Info, id: int) -> Optional[StationType]:
        """Fetches a single station by its ID."""
        db = info.context["db"]
        station = await StationService.get_by_id(db, station_id=id)
        return StationType(**station.dict()) if station else None

    @strawberry.field
    async def stations(self, info: Info, skip: int = 0, limit: int = 10) -> Connection[StationType]:
        """Fetches a paginated list of stations."""
        db = info.context["db"]
        stations, total_count = await StationService.get_all_paginated(db, skip, limit)
        
        edges = [
            Edge(node=StationType(**station.dict()), cursor=str(skip + i))
            for i, station in enumerate(stations)
        ]

        page_info = PageInfo(
            has_next_page=skip + limit < total_count,
            has_previous_page=skip > 0,
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-1].cursor if edges else None,
        )
        
        return Connection(total_count=total_count, edges=edges, page_info=page_info)