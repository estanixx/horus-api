import strawberry
from typing import Generic, List, TypeVar, Optional

T = TypeVar("T")

@strawberry.type
class PageInfo:
    """Information about pagination in a connection."""
    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str]
    end_cursor: Optional[str]

    @classmethod
    def from_skip_limit(cls, skip: int, limit: int, total: int) -> "PageInfo":
        """Helper method to create PageInfo from skip/limit pagination."""
        has_previous_page = skip > 0
        has_next_page = skip + limit < total
        return cls(
            has_next_page=has_next_page,
            has_previous_page=has_previous_page,
            start_cursor=str(skip) if total > 0 else None,
            end_cursor=str(skip + min(limit, total) - 1) if total > 0 else None,
        )

@strawberry.type
class Edge(Generic[T]):
    """An edge in a connection."""
    node: T
    cursor: str

@strawberry.type
class Connection(Generic[T]):
    """A connection to a list of items."""
    total_count: int
    edges: List[Edge[T]]
    page_info: PageInfo