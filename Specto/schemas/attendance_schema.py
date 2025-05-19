from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from Specto.schemas import TimeStamp


class TimeInSchema(TimeStamp):
    user_id: str
    time_in: Optional[datetime] = None
    time_out: Optional[datetime] = None
    clock_type: Optional[str] = None
