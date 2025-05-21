import strawberry
from typing import Optional

@strawberry.type
class Song:
    id: int
    name: str = strawberry.field(resolver=lambda: "Lonely day")
    artist: str
    year: Optional[int] = None

