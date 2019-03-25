from flask import Flask, Blueprint
from flask_restplus import Api, Resource, fields
from environment.instance import Config

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api/1')
        self.api = Api(self.blueprint,
            version='1.0',
            title='Sample Book API',
            description='A simple Book API',
            doc = self.app.config["SWAGGER_URL"]
        )

    def run(self):
        # self.app.run()
        self.app.run(
                debug = self.app.config["DEBUG"],
                port = self.app.config["PORT"],
                host = self.app.config["HOST"]
            )

server = Server()
