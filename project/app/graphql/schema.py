# app/graphql/schema.py
import strawberry
from app.graphql.queries import Query # Import the combined Query type
from app.graphql.mutations import Mutation # Import the combined Mutation type

schema = strawberry.Schema(query=Query, mutation=Mutation)