from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlmodel import Field, SQLModel
        
class TimestampsSQLModel(SQLModel):

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False
        ),
        description="Creation timestamp in UTC."
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            onupdate=lambda: datetime.now(timezone.utc)
        ),
        description="Timestamp of the last update to the record (UTC)."
    )

    class Config:
        arbitrary_types_allowed = True
        

class BaseSQLModel(TimestampsSQLModel):
    id: int = Field(
        default=None,
        primary_key=True,
        description="Primary record key"
    )
