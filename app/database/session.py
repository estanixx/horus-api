# app/database/session.py
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
# Load the database connection URL from environment variables for security and flexibility.
# Example: "postgresql+asyncpg://user:password@host/dbname"

# Create the asynchronous engine for interacting with the database.
# echo=True will log all SQL statements issued, which is useful for debugging.
# future=True enables SQLAlchemy 2.0 style usage.
engine = AsyncEngine(create_engine(settings.DATABASE_URL, echo=True, future=True))


async def init_db():
    """
    Initializes the database by creating all tables.

    This function connects to the database using the engine and creates all tables
    defined by the SQLModel metadata. It should typically be called once
    on application startup to set up the database schema.
    """
    async with engine.begin() as conn:
        # The following line can be uncommented to drop all tables, useful for a clean reset during development.
        # await conn.run_sync(SQLModel.metadata.drop_all)
        
        # This command creates all tables that inherit from SQLModel.
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
    # Create a factory for asynchronous session objects.
    # expire_on_commit=False is recommended for async sessions to prevent
    # objects from being expired after a commit, allowing them to be used further.
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    # The 'async with' block ensures the session is properly closed after use.
    async with async_session() as session:
        # Yield the session to the dependent function. The code within the
        # dependent function will execute here.
        yield session