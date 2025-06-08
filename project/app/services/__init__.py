# app/services/__init__.py
"""
Service Layer Barrel File.

This module serves as a convenient entry point to the service layer. It
imports and re-exports all individual service classes from this directory.

This allows other parts of the application (like the GraphQL resolvers) to
import any service with a single, clean import statement, for example:
`from app.services import StationService, CameraService`
"""

# Import service classes to make them accessible from the app.services package.
from .station_service import StationService
from .camera_service import CameraService

# Define the public API for this package for wildcard imports (e.g., from app.services import *).
__all__ = [
    "StationService",
    "CameraService",
]