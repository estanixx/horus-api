# app/graphql/schema.py
"""
Main GraphQL Schema Definition.

This module is the central point where the entire GraphQL schema is assembled.
It imports the root Query and Mutation types, each of which aggregates its
respective fields from other modules.

The final `schema` object is then exported to be used by the web server
integration (e.g., in the main FastAPI application) to handle GraphQL requests.
"""

import strawberry

# Import the root Query and Mutation types, which have been aggregated
# in their respective __init__.py files.
from .queries import Query
from .mutations import Mutation

# Create the final, executable GraphQL schema by passing the root
# Query and Mutation types to the strawberry.Schema constructor.
# This object contains all the information about your API's capabilities.
schema = strawberry.Schema(query=Query, mutation=Mutation)