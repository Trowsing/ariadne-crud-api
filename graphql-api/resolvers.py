from ariadne import make_executable_schema, QueryType, MutationType
from database import Person


type_defs = """
    type Query {
        hello: String!
        people: [Person!]!
    }

    type Mutation {
        create_person(name: String!, age: Int!, last_name: String!): Person!
		get_person(id: Int!): Person!
		delete_person(id: Int!): Person
    }

    type Person {
        id: Int
        age: Int
        name: String
        last_name: String
    }
"""

query = QueryType()
mutation = MutationType()


@query.field("hello")
def resolve_hello(_, info):
    request = info.context
    user_agent = request.headers.get("User-Agent", "Guest")
    return f"Hello, {user_agent}!"


@query.field("people")
def resolve_people(_, info):
    return Person.query.all()


@mutation.field("get_person")
def resolve_get_person(_, info, id):
    return Person.query.filter_by(id=id).first()


@mutation.field("create_person")
def resolve_create_person(_, info, name, age, last_name):
    person = Person.create(name, last_name, age)
    return person


@mutation.field("delete_person")
def resolve_delete_person(_, info, id):
    return Person.delete(id=id)


schema = make_executable_schema(type_defs, query, mutation)
