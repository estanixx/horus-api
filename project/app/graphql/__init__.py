# app/graphql/__init__.py

from .schema import schema
from .context import get_context

# Optionally re-export Query and Mutation types for convenience
from .queries import Query
from .mutations import Mutation

__all__ = ["schema", "get_context", "Query", "Mutation"]