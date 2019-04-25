from .graph_object import Team
from .model import GraphModel


class TeamModel(GraphModel):
    """Techno model to handle techno node and related object"""
    def __init__(self, server):
        super().__init__(server, Team)

    def get(self, name, one=True):
        """Get one or more techno"""
        if one:
            return self.graph_object.select(self.graph, name).first()
        else:
            return list(self.graph_object.select(self.graph).where("_.name =~ '{}.*'".format(name)))

    def post(self, data):
        """Add one techno"""
        team = self.graph_object()
        team.name = data.get("name", "")
        team.type = data.get("type", "")
        team.tagline = data.get("tagline", "")
        self.graph.push(team)
        return data

    def put(self, name, data):
        """Update one techno"""
        selection = self.graph_object.select(self.graph, name).first()
        if not selection:
            return None

        if data:
            selection.name = data.get("name", "")
            selection.type = data.get("type", "")
            selection.tagline = data.get("tagline", "")
            self.graph.push(selection)
            return selection

        return None

    def delete(self, name):
        """Delete one techno"""
        selection = self.get(name)
        if not selection:
            return None

        for target in self.relation(rel="persons", name=name, target="person")[0]["person"]:
            selection.__getattribute__("persons").remove(target)
        self.graph.push(selection)
        self.graph.delete(selection)
        return selection

    def relation(self, rel, name=None, target=None):
        """Get related GraphObject"""
        selection = self.lists
        if name:
            selection = self.get(name, one=False)

        return super().relation(rel=rel, selection=selection, target=target)

