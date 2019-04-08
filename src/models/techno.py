from .graph_object import Techno
from .model import GraphModel


class TechnoModel(GraphModel):
    """Techno model to handle techno node and related object"""
    def __init__(self, graph, api):
        super().__init__(graph, api, Techno)

    def get(self, name, one=True):
        """Get one or more techno"""
        if one:
            return self.graph_object.select(self.graph, name).first()
        else:
            return list(self.graph_object.select(self.graph).where("_.name =~ '{}.*'".format(name)))

    def post(self, data):
        """Add one techno"""
        techno = self.graph_object()
        techno.name = data.get("name", "")
        techno.type = data.get("type", "")
        techno.description = data.get("description", "")
        self.graph.push(techno)
        return data

    def put(self, name, data):
        """Update one techno"""
        selection = self.graph_object.select(self.graph, name).first()
        if not selection:
            return None

        if data:
            selection.name = data.get("name", "")
            selection.type = data.get("type", "")
            selection.description = data.get("description", "")
            self.graph.push(selection)
            return selection

        return None

    def delete(self, name):
        """Delete one techno"""
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

