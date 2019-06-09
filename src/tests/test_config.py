import unittest
import os
from flask import current_app
from flask_testing import TestCase
from src.server.instance import Server
from src.environment.instance import config


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        server = Server(config["dev"])
        return server.app

    def test_app_is_development(self):
        self.assertTrue(self.create_app().config['SECRET_KEY'] is 'secret_key')
        self.assertTrue(self.create_app().config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            self.create_app().config['NEO4J_DATABASE_URL'] == os.environ.get("NEO4J_DATABASE_URL") + "/db/data/"
        )
        self.assertTrue(
            self.create_app().config['NEO4J_DATABASE_IP'] == os.environ.get("NEO4J_DATABASE_IP") + " /db/data/"
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        _server = Server(config["test"])
        _server.app.config.from_object(config['test'])
        return _server.app

    def test_app_is_testing(self):
        self.assertTrue(self.create_app().config['SECRET_KEY'] is 'secret_key')
        self.assertTrue(self.create_app().config['DEBUG'])
        self.assertFalse(current_app is None)
        self.assertTrue(
            self.create_app().config['NEO4J_DATABASE_URL'] == os.environ.get("NEO4J_DATABASE_URL_TEST") + "/db/data/"
        )
        self.assertTrue(
            self.create_app().config['NEO4J_DATABASE_IP'] == os.environ.get("NEO4J_DATABASE_IP_TEST") + " /db/data/"
        )


if __name__ == '__main__':
    unittest.main()