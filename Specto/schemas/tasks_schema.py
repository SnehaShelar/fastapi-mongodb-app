from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime
from Specto.common.constants import StatusConstants
from bson import ObjectId


class TaskCreateSchema(BaseModel):
    title: str
    description: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    project_id: Optional[str] = Field(alias="_id", default=None)
    status: StatusConstants = Field(default=StatusConstants.Todo.value)
    estimated_hours: Optional[str] = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by: Optional[str] = Field(alias="_id", default=None)

    class Config:
        arbitrary_types_allowed = True
        populate_by_name = True
        json_encoders = {
            ObjectId: str,
            StatusConstants: lambda v: v.value,
        }
