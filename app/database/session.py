"""
Database session management for the application.

This module handles the configuration and creation of the database engine
and provides a session factory for dependency injection into the application's
services and resolvers, configured for asynchronous operations.
"""

import os
from typing import AsyncGenerator

from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from app.core.config import settings

engine = AsyncEngine(create_engine(settings.DATABASE_URL, echo=True, future=True))


async def init_db():
    """
    Initializes the database by creating all tables.

    This function connects to the database using the engine and creates all tables
    defined by the SQLModel metadata. It should typically be called once
    on application startup to set up the database schema.
    """
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Asynchronous generator that provides a database session.

    This function is designed to be used as a dependency (e.g., with FastAPI's
    `Depends`) to provide a new `AsyncSession` for each request. It ensures
    that the session is always closed properly after the request is handled.

    Yields:
        An `AsyncSession` object for performing database operations.
    """
    
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session