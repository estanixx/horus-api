# app/graphql/services/camera_service.py

"""
Service layer for handling business logic related to Camera models.
"""

from typing import List, Optional, Tuple
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import func, and_
import strawberry
from app.models import Camera
from typing import TYPE_CHECKING, Annotated
if TYPE_CHECKING:
    from app.graphql.types import CameraCreateInput, CameraUpdateInput


class CameraService:
    """Service class for camera-related operations."""

    @staticmethod
    async def get_by_id(db: AsyncSession, camera_id: int) -> Optional[Camera]:
        """
        Retrieves a single camera by its ID, pre-loading the parent station.
        """
        statement = (
            select(Camera)
            .where(Camera.id == camera_id)
        )
        result = await db.exec(statement)
        return result.first()

    @staticmethod
    async def get_for_station(
        db: AsyncSession, station_id: int, skip: int, limit: int
    ) -> Tuple[List[Camera], int]:
        """
        Retrieves a paginated list of cameras for a specific station and the total count.
        """
        statement = (
            select(Camera)
            .where(Camera.station_id == station_id)
            .offset(skip)
            .limit(limit)
        )
        result = await db.exec(statement)
        cameras = result.all()
        
        count_statement = select(func.count()).select_from(Camera).where(Camera.station_id == station_id)
        total_count = (await db.exec(count_statement)).one()
        
        return cameras, total_count

    @staticmethod
    async def get_all_paginated(
        db: AsyncSession, skip: int, limit: int
    ) -> Tuple[List[Camera], int]:
        """
        Retrieves a paginated list of all cameras.
        """
        statement = select(Camera).offset(skip).limit(limit)
        result = await db.exec(statement)
        cameras = result.all()

        count_statement = select(func.count()).select_from(Camera)
        total_count = (await db.exec(count_statement)).one()

        return cameras, total_count
        
    @staticmethod
    async def create(db: AsyncSession, data:  Annotated["CameraCreateInput", strawberry.lazy('app.graphql.types')]) -> Camera: # Or SensorCreateInput
        """Creates a new camera."""
        # Explicitly convert the input object to a dictionary for validation
        new_model = Camera(**strawberry.asdict(data))
        
        db.add(new_model)
        await db.commit()
        await db.refresh(new_model)
        return new_model

    @staticmethod
    async def update(db: AsyncSession, camera_id: int, data:  Annotated["CameraUpdateInput", strawberry.lazy('app.graphql.types')]) -> Optional[Camera]:
        """Updates an existing camera."""
        camera = await db.get(Camera, camera_id)
        if not camera:
            return None

        update_data = strawberry.asdict(data)
        for key, value in update_data.items():
            setattr(camera, key, value)

        db.add(camera)
        await db.commit()
        await db.refresh(camera)
        return camera

    @staticmethod
    async def delete(db: AsyncSession, camera_id: int) -> Optional[Camera]:
        """Deletes a camera."""
        camera = await db.get(Camera, camera_id)
        if not camera:
            return None
        
        await db.delete(camera)
        await db.commit()
        return camera