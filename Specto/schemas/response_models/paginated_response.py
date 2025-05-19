from typing import List, Generic, TypeVar, Optional
from pydantic.generics import GenericModel
from pydantic import BaseModel

T = TypeVar('T')

class PaginationInfo(BaseModel):
    currentPage: int
    totalCount: int
    totalPages: int
    hasPrevious: bool
    hasNext: bool

class PaginatedResponse(GenericModel, Generic[T]):
    success: bool = True
    data: List[T]
    pagination: PaginationInfo
    message: str = "Success"
    errors: List[str] = []

