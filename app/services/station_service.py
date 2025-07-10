# app/graphql/services/station_service.py

"""
Service layer for handling business logic related to Station models.
"""
from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import func
import strawberry

from app.models import Station
from typing import TYPE_CHECKING, Annotated
if TYPE_CHECKING:
    from app.graphql.types import StationCreateInput, StationUpdateInput

class StationService:
    """Service class for station-related operations."""

    # ... (get_all_paginated and get_by_id methods are unchanged) ...

    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[Station], int]:
        statement = select(Station).offset(skip).limit(limit)
        result = await db.exec(statement)
        stations = result.all()
        
        count_statement = select(func.count()).select_from(Station)
        total_count = (await db.exec(count_statement)).one()
        
        return stations, total_count

    @staticmethod
    async def get_by_id(db: AsyncSession, station_id: int) -> Optional[Station]:
        statement = (
            select(Station)
            .where(Station.id == station_id)
        )
        result = await db.exec(statement)
        return result.first()
    
    @staticmethod
    async def create(db: AsyncSession, data: Annotated["StationCreateInput", strawberry.lazy('app.graphql.types')]) -> Station:
        """Creates a new station."""
        # Explicitly convert the input object to a dictionary for validation
        new_model = Station(**strawberry.asdict(data))
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @staticmethod
    async def update(db: AsyncSession, station_id: int, data:  Annotated["StationUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[Station]:
        """Updates an existing station."""
        station = await db.get(Station, station_id)
        if not station:
            return None

        # Get dictionary of fields to update, excluding unset values
        update_data = strawberry.asdict(data)
        for key, value in update_data.items():
            setattr(station, key, value)

        db.add(station)
        await db.commit()
        await db.refresh(station)
        return station

    @staticmethod
    async def delete(db: AsyncSession, station_id: int) -> Optional[Station]:
        """Deletes a station."""
        station = await db.get(Station, station_id)
        if not station:
            return None
            
        await db.delete(station)
        await db.commit()
        return station