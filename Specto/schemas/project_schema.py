from pydantic import BaseModel
from typing import Optional


class Project(BaseModel):
    #  id: Optional[str] = Field(alias="_id", default=None)
     name: str
     description: Optional[str] = None

     class Config:
        populate_by_name = True
        # json_encoders = {ObjectId: str}  # ✅ Auto-convert ObjectId to str