# app/graphql/__init__.py
"""
GraphQL Package Entry Point.

This file serves as the main public interface for the GraphQL package.
It aggregates the final schema, the context getter, and the root operation
types (Query and Mutation) from their respective sub-modules.

This allows the main application server (e.g., FastAPI) to import all
necessary GraphQL components from a single, convenient location: `app.graphql`.
"""

# Import the final assembled schema and the context getter function,
# which are the primary components needed by the web server integration.
from .schema import schema
from .context import get_context

# Optionally re-export the root Query and Mutation types. This can be
# useful for type hinting or for tools that inspect the schema structure.
from .queries import Query
from .mutations import Mutation

# Define the public API for the 'app.graphql' package. When another module
# uses `from app.graphql import *`, only these names will be imported.
__all__ = ["schema", "get_context", "Query", "Mutation"]