from pydantic import BaseModel, Field
from datetime import datetime, UTC


class TimeStamp(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
