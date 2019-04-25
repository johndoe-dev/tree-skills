from .graph_object import Person
from .model import GraphModel


class PersonModel(GraphModel):
    """Person model to handle person node and related object"""
    def __init__(self, server):
        super().__init__(server, Person)

    def get(self, name, one=True):
        """get one or more person(s)"""
        person = list(self.graph_object.select(self.graph).where("_.name =~ '{}.*'".format(name)))
        if one:
            person = self.graph_object.select(self.graph, name).first()

        return person

    def post(self, data):
        """Add one person"""
        person = self.graph_object()
        person.name = data.get("name", "")
        self.graph.push(person)
        return data

    def put(self, name, data):
        """Update one person"""
        selection = self.get(name)
        if not selection:
            return None
        if data:
            selection.name = data.get("name", "")
            self.graph.push(selection)
            return selection

    def delete(self, name):
        """Delete one person"""
        selection = self.get(name)
        if not selection:
            return None
        self.graph.delete(selection)
        return selection

    def relation(self, rel, name=None, target=None):
        """Get related GraphObject"""
        selection = self.lists
        if name:
            selection = self.get(name, one=False)
        return super().relation(rel=rel, selection=selection, target=target)

    def add_relation(self, rel, source_name, target_object):
        """Create relation with GraphObject"""
        selection = self.get(source_name)
        if super().add_relation(rel, selection, target_object):
            return self.relation(rel, source_name)
        return None

    def delete_relation(self, rel, source_name, target_object):
        """Delete relation with GraphObject"""
        selection = self.get(source_name)
        selection.__getattribute__(rel).remove(target_object)
        self.graph.push(selection)


