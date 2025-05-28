# app/graphql/mutations/__init__.py
import strawberry
from .station_mutation import StationMutation
from .camera_mutation import CameraMutation

# Combine all individual mutation types into a single root Mutation type
@strawberry.type
class Mutation(StationMutation, CameraMutation):
    pass