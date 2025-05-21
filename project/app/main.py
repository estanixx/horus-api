from fastapi import Depends, FastAPI
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db import get_session
from app.schemas.main import *
from strawberry.fastapi import GraphQLRouter
from typing import List
import strawberry

async def get_context(
    session: AsyncSession = Depends(get_session),
) -> dict:
    return {
        'session': session,
    }


@strawberry.type
class Query:
    songs: List[Song]
    
schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

@app.get("/ping")
async def pong():
    return {"ping": "aaaa!"}

