# app/graphql/context.py
from typing import Dict, Any
from sqlmodel import Session
from app.database.session import get_session # Assuming your session logic is here

async def get_context() -> Dict[str, Any]:
    # This generator function will be called for each request
    # and provide a database session to your resolvers
    async for session in get_session():
        yield {"db": session}

# If you prefer a synchronous context getter (e.g., if you're not using async/await for db session)
# def get_sync_context() -> Dict[str, Any]:
#     # Assuming get_session is synchronous
#     return {"db": next(get_session())}