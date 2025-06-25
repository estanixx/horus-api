import strawberry
from typing import Optional
from app.graphql.types import CameraType, CameraCreateInput, CameraUpdateInput
from app.models import Sensor
from app.services import SensorService
from sqlmodel.ext.asyncio.session import AsyncSession

# @strawberry.type
# class SensorMutation:
    
    