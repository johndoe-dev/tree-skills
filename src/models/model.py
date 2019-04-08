from abc import abstractmethod


class GraphModel(object):
    """Class to handle update to database"""
    def __init__(self, graph, api, class_name):
        self.api = api
        self.graph = graph
        self.graph_object = class_name

    @classmethod
    def api(cls):
        return cls.api()

    @staticmethod
    def items(selection):
        return dict(selection._GraphObject__ogm.__dict__["node"]).items()

    @property
    def lists(self):
        """Return all list of GraphObject"""
        selection = self.graph_object.select(self.graph)
        list_selection = [s for s in selection]
        return list_selection

    @abstractmethod
    def get(self, **prop):
        pass

    @abstractmethod
    def post(self, **prop):
        pass

    @abstractmethod
    def put(self, **prop):
        pass

    @abstractmethod
    def delete(self, **prop):
        pass

    def model(self, model):
        """Get model to use with swagger"""
        return self.api.models[model]

    def relation(self, rel, selection, target=None):
        """Get related object"""
        # Init empty list of selection
        list_selection = []
        # Init target name of relation
        target_name = target
        # For each selection
        for i, select in enumerate(selection):
            # Append person to list of persons
            selection_name = select.__class__.__name__.replace("Selection", "").lower()
            list_selection.append({
                selection_name: {k: v for k, v in self.items(select)}
            })
            # Init list of target from relation
            # Example: Techno
            targets = []
            # If relation exists
            if select.__getattribute__(rel):
                # For each target of relation
                for target in select.__getattribute__(rel):
                    # Create dictionary of target
                    # Example : {"name": "NeO4j", "type": "Database", "Description": "Graph database"}
                    sub_target = {k: v for k, v in self.items(target)}
                    # Append target dictionary to targets list
                    # Example: [{"name": "Neo4j",...},{…},…]
                    targets.append(sub_target)
                    # get class name of targets
                    # Example: "techno"
                    if not target_name:
                        target_name = target.__class__.__name__.lower()
            # Append each person to list of persons
            list_selection[i][target_name] = targets
        return list_selection

    def add_relation(self, rel, selection, target):
        selection.__getattribute__(rel).add(target)
        self.graph.push(selection)
        if self.check_relation(rel, selection, target):
            return True
        return False

    def check_relation(self, rel, selection, target):
        target = {k: v for k, v in self.items(target)}
        if selection.__getattribute__(rel):
            for t in selection.__getattribute__(rel):
                sub_target = {k: v for k, v in self.items(t)}
                if target == sub_target:
                    return True

        return False
