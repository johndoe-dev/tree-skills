from flask_testing import TestCase
from environment.instance import config
from server.instance import Server
from models.person import PersonModel
from models.team import TeamModel
from models.techno import TechnoModel


class BaseTestCase(TestCase):
    """ Base Tests """
    server = Server(config["test"])
    person = None
    team = None
    techno = None

    def create_app(self):
        return self.server.app

    def setUp(self):
        self.server.database.create_all()
        self.person = PersonModel(graph=self.server.graph, api=self.server.api)
        self.team = TeamModel(graph=self.server.graph, api=self.server.api)
        self.techno = TechnoModel(graph=self.server.graph, api=self.server.api)

    def tearDown(self):
        self.server.database.delete_all()
