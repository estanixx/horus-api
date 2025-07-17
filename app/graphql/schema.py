import strawberry
from strawberry.schema.config import StrawberryConfig
from .queries import Query
from .mutations import Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=False))