from flask import Flask, Blueprint
from flask_script import Manager
from flask_restplus import Api
from environment.instance import config
from database.neo4j import Database


class Server(object):
    def __init__(self, config):
        self._app = Flask(__name__)
        self._app.config.from_object(config)
        self._database = Database(self._app)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api/1')
        self._api = Api(
            self.blueprint,
            version='1.0',
            title='Sample Book API',
            description='A simple Book API',
            doc=self._app.config["SWAGGER_URL"],
            ordered=True
        )

        self._app.register_blueprint(self.blueprint)

        self.manager = Manager(self._app)

    @property
    def app(self):
        return self._app

    @property
    def api(self):
        return self._api

    @property
    def database(self):
        return self._database

    @property
    def graph(self):
        return self._database.graph

    def add_namespaces(self, *namespaces):
        for namespace in namespaces:
            self._api.add_namespace(namespace)

    def run(self):
        # self.app.run()
        self._app.run(
                debug=self.app.config["DEBUG"],
                port=self.app.config["PORT"],
                host=self.app.config["HOST"]
            )


server = Server(config["dev"])
