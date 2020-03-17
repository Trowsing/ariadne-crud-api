from ariadne import QueryType, MutationType
from database import Person


query = QueryType()
mutation = MutationType()


@query.field("hello")
def resolve_hello(_, info):
    """Returns a hello message with User-Agent's property."""
    request = info.context
    user_agent = request.headers.get("User-Agent", "Guest")
    return f"Hello, {user_agent}!"


@query.field("people")
def resolve_people(_, info):
    """Queries all persons in the database."""
    return Person.query.all()


@mutation.field("get_person")
def resolve_get_person(_, info, id):
    """Queries a single person in the database by ID."""
    return Person.query.filter_by(id=id).first()


@mutation.field("create_person")
def resolve_create_person(_, info, name, age, last_name):
    """Creates a new person in the database."""
    person = Person.create(name, last_name, age)
    return person


@mutation.field("delete_person")
def resolve_delete_person(_, info, id):
    """Removes a given person from the database."""
    return Person.delete(id=id)
