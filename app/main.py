# app/main.py
"""
Main FastAPI Application File.

This module serves as the primary entry point for the web application.
It is responsible for:
- Creating and configuring the FastAPI app instance.
- Setting up CORS middleware to allow cross-origin requests from the frontend.
- Managing application lifespan events, like initializing the database on startup.
- Mounting the Strawberry GraphQL router to handle all GraphQL requests.
- Defining any simple REST endpoints, such as a health check.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from app.core.config import settings
from app.graphql import get_context, schema

# --- FastAPI App Initialization ---

# Create the main FastAPI application instance.
# The title is loaded from the configuration settings.
app = FastAPI(title=settings.PROJECT_NAME)


# --- CORS (Cross-Origin Resource Sharing) Middleware ---

# Define the list of origins that are allowed to make requests to this API.
# In development, this is typically your frontend application's URL.
origins = [
    "http://localhost:3000",
]

# Add the CORS middleware to the application.
# This is necessary to allow your Next.js frontend to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # Allow requests from the origins specified above.
    allow_credentials=True,     # Allow cookies to be included in requests.
    allow_methods=["*"],        # Allow all HTTP methods (GET, POST, etc.).
    allow_headers=["*"],        # Allow all HTTP headers.
)



# --- GraphQL Router Setup ---

# Create the GraphQL router, which will handle all GraphQL requests.
graphql_app = GraphQLRouter(
    schema=schema,                  # The assembled Strawberry GraphQL schema.
    context_getter=get_context,     # The function that provides the request context (e.g., DB session).
    graphiql=True                   # Enable the GraphiQL interactive API browser.
)

# Mount the GraphQL router at a specific path.
# All GraphQL operations will be available at http://.../graphql
app.include_router(graphql_app, prefix="/graphql")


# --- REST Endpoints ---

@app.get("/health")
async def health_check():
    """
    Simple health check endpoint.

    Used to verify that the application server is running and responsive.
    """
    return {"status": "ok"}

# To run this application from your terminal:
# uvicorn app.main:app --reload