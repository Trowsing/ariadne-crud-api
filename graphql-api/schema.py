from ariadne import load_schema_from_path, make_executable_schema
from resolvers import query, mutation


type_defs = load_schema_from_path("types/")

schema = make_executable_schema(type_defs, query, mutation)
