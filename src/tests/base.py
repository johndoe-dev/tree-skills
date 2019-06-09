from flask_testing import TestCase
from src.environment.instance import config
from src.server.instance import Server
from src.models.person import PersonModel
from src.models.team import TeamModel
from src.models.techno import TechnoModel


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
        self.person = PersonModel(self.server)
        self.team = TeamModel(self.server)
        self.techno = TechnoModel(self.server)

    def tearDown(self):
        self.server.database.delete_all()
