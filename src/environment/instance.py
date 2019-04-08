import os
from dotenv import load_dotenv


basedir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../.env"))
load_dotenv(basedir)


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret_key"
    DEBUG = False
    PORT = 5000
    HOST = "0.0.0.0"
    # Database auth
    NEO4J_DATABASE_USERNAME = "neo4j"
    NEO4J_DATABASE_PWD = "test"
    SWAGGER_URL = "/"


class DevelopmentConfig(Config):
    DEBUG = True
    # Database connections
    NEO4J_DATABASE_URL = os.environ.get("NEO4J_DATABASE_URL") + "/db/data/"
    NEO4J_DATABASE_IP = os.environ.get("NEO4J_DATABASE_IP") + " /db/data/"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # Database connections
    NEO4J_DATABASE_URL = os.environ.get("NEO4J_DATABASE_URL_TEST") + "/db/data/"
    NEO4J_DATABASE_IP = os.environ.get("NEO4J_DATABASE_IP_TEST") + " /db/data/"


config = dict(
    dev=DevelopmentConfig,
    test=TestingConfig
)
