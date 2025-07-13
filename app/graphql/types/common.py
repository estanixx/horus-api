"""
Defines common, reusable GraphQL types, such as for pagination.

This module implements a generic pagination structure based on the GraphQL
Cursor Connections Specification. This allows for consistent and efficient
pagination across all relevant queries in the API.
"""

from typing import List, Generic, TypeVar
import strawberry

T = TypeVar("T")

@strawberry.type
class PageInfo:
    """
    Contains information about the current page of results in a paginated response,
    enabling navigation.
    """
    has_next_page: bool = strawberry.field(description="Indicates if there are more items after this page.")
    has_previous_page: bool = strawberry.field(description="Indicates if there are items before this page.")
    start_cursor: str | None = strawberry.field(description="The cursor for the first item on the page.")
    end_cursor: str | None = strawberry.field(description="The cursor for the last item on the page.")

@strawberry.type
class Edge(Generic[T]):
    """
    Represents a single node in a paginated list, connecting the node itself
    with its pagination cursor.
    """
    cursor: str = strawberry.field(description="A unique cursor for this item.")
    node: T = strawberry.field(description="The actual data item.")

@strawberry.type
class Connection(Generic[T]):
    """
    Represents a paginated list of items, including the items themselves (as edges)
    and information about the current page.
    """
    total_count: int = strawberry.field(description="The total number of items in the entire list.")
    edges: List[Edge[T]] = strawberry.field(description="A list of edges, each containing a node and its cursor.")
    page_info: PageInfo = strawberry.field(description="Information to aid in pagination.")