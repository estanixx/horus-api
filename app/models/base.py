# app/models/base.py
"""
Base SQLModel Definition.

This module defines a `BaseSQLModel` class that serves as the foundation for
all other database models in the application. It includes common, automatically
managed fields such as `id`, `created_at`, and `updated_at`.
"""

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlmodel import Field, SQLModel


class BaseSQLModel(SQLModel):
    """
    A base class for all SQLModel tables.

    Provides common, auto-populated fields for a primary key, creation timestamp,
    and update timestamp. All timestamps are timezone-aware and stored in UTC.

    Attributes:
        id (Optional[int]): The primary key for the record. Auto-populated by the database.
        created_at (datetime): Timestamp of when the record was created. Auto-populated.
        updated_at (datetime): Timestamp of the last update. Auto-updated by the database.
    """
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        description="The primary key for the record."
    )

    # CORRECTED: Switched to timezone-aware datetimes to prevent database errors.
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column=Column(
            TIMESTAMP(timezone=True),  # Ensures the database column type is TIMESTAMPTZ.
            nullable=False
        ),
        description="Timestamp of when the record was created (UTC)."
    )

    # CORRECTED: Switched to timezone-aware datetimes and combined SQLAlchemy arguments.
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            onupdate=lambda: datetime.now(timezone.utc)  # This tells the DB to update on modification.
        ),
        description="Timestamp of the last update to the record (UTC)."
    )

    class Config:
        """Pydantic model configuration."""
        # Allows the model to use custom types that might not be natively supported by Pydantic.
        arbitrary_types_allowed = True