from math import ceil
from typing import Any, List

def build_paginated_response(data: List[Any], page: int, limit: int, total_count: int, message: str = "Success") -> dict:
    total_pages = ceil(total_count / limit)
    return {
        "data": data,
        "pagination": {
            "currentPage": page,
            "totalCount": total_count,
            "totalPages": total_pages,
            "hasPrevious": page > 1,
            "hasNext": page < total_pages
        },
    }

