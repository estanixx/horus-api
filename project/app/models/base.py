# app/models/base.py
from datetime import datetime, timezone
from typing import Optional
from sqlmodel import Field, SQLModel

class BaseSQLModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": lambda: datetime.now(timezone.utc)}, nullable=False)

    class Config:
        arbitrary_types_allowed = True 