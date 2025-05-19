from pydantic import BaseModel
from typing import Any, List, Optional


class UserResponse(BaseModel):
    id: str
    email: str
    

class ResponseModel(BaseModel):
    success: bool = True
    data: Optional[Any] = None
    message: str = ""
    errors: List[str] = []
