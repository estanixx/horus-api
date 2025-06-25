"""
FastAPI Application Entry Point.

Responsibilities:
- Creates and configures FastAPI app instance
- Sets up CORS middleware for cross-origin requests
- Mounts Strawberry GraphQL router
- Provides basic REST endpoints (health check)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from app.core.config import settings
from app.graphql import get_context, schema

ALLOWED_ORIGINS = [
    "http://localhost:3000",
]


def create_app() -> FastAPI:
    """Factory function to create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="FastAPI backend with GraphQL endpoint"
    )

    configure_cors(app)
    setup_graphql(app)
    add_routes(app)

    return app


def configure_cors(app: FastAPI) -> None:
    """Configure CORS middleware for the application."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[ALLOWED_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def setup_graphql(app: FastAPI) -> None:
    """Configure and mount GraphQL router."""
    graphql_app = GraphQLRouter(
        schema=schema,
        context_getter=get_context,
        graphiql=True
    )
    app.include_router(graphql_app, prefix="/graphql")


def add_routes(app: FastAPI) -> None:
    """Add REST endpoints to the application."""
    
    @app.get("/health")
    async def health_check() -> dict:
        """Health check endpoint."""
        return {"status": "ok"}


# Main application instance
app = create_app()