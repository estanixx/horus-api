"""
GraphQL Request Context Factory.

This module is responsible for creating the context object that is available
in all Strawberry GraphQL resolvers. The primary purpose of the context is
to provide shared resources, such as a database session, to the resolvers
in a clean and managed way for each request.
"""

from typing import Dict, Any, AsyncGenerator

from app.database.session import get_session  
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_context() -> AsyncGenerator[Dict[str, Any], None]:
    """
    Asynchronous generator to create the GraphQL request context.

    This function is called once per request. It creates a new database session
    for the duration of the request and "yields" it in a dictionary.
    This generator pattern, combined with FastAPI's dependency injection, ensures
    that the session is properly created before the request and closed after.

    Yields:
        A dictionary containing the database session (`AsyncSession`) accessible
        via the key "db" in the resolver's `info.context`.
    """
    
    async for session in get_session():
        yield {"db": session}

# If you prefer a synchronous context getter (e.g., if you're not using async/await for db session)
# from sqlmodel import Session
#
# def get_sync_context() -> Dict[str, Any]:
# 	  """Synchronous context getter for non-async applications."""
#     # Assuming get_session is synchronous and yields a session
#     db: Session = next(get_session())
#     return {"db": db}