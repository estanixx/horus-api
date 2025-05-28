# app/main.py
from fastapi import FastAPI, Depends
from strawberry.fastapi import GraphQLRouter
import uvicorn

from app.graphql.schema import schema
from app.database.session import get_session
from app.graphql.context import get_context # Your custom context getter
from app.core.config import settings # Assuming you have a config for app details


app = FastAPI(title=settings.PROJECT_NAME)

# Create tables on startup (only for development/initial setup, use Alembic for migrations in prod)


# Setup GraphQL endpoint
graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context, # Provide your context getter
    graphiql=True # Enable GraphiQL UI for easy testing
)

app.include_router(graphql_app, prefix="/graphql")

@app.get("/health")
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}

# To run this app:
# uvicorn app.main:app --reload