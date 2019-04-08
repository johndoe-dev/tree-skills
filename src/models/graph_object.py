from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom


class Person(GraphObject):
    """Person GraphObject to create Person node

    Example of uses:
    get a list of persons:
    '''
    selection = Person.select(graph)
    persons = [s for s in selection]
    return persons
    '''

    get one person
    '''
    person = Person.select(graph, "John").first()
    '''

    update one person
    '''
    person.name = "John"
    '''

    Delete one person
    '''
    graph.delete(person)
    '''
    """
    __primarykey__ = "name"

    """All property"""
    name = Property()

    """All relation """
    JAM_WITH = RelatedTo("Techno")
    PLAYED_IN = RelatedTo("Team")


class Techno(GraphObject):
    """Techno GraphObject to create Techno node"""
    __primarykey__ = "name"

    """All property"""
    name = Property()
    type = Property()
    description = Property()

    """All relation """
    persons = RelatedFrom("Person", "JAM_WITH")


class Team(GraphObject):
    """Team GraphObject to create Team node"""
    __primarykey__ = "name"

    """All property"""
    name = Property()
    type = Property()
    tagline = Property()

    """All relation """
    persons = RelatedFrom("Person", "PLAYED_IN")

