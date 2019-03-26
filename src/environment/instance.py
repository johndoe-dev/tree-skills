import os
from dotenv import load_dotenv


basedir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../.env"))
load_dotenv(basedir)


class Config(object):
    # Load the development "mode". Use "development" if not specified
    __env = os.environ.get("PYTHON_ENV", "development")

    __all_environments = {
        "development": {"port": 5000, "host": "0.0.0.0", "debug": True, "swagger-url": "/"},
        "production": {"port": 8080, "host": "0.0.0.0", "debug": False, "swagger-url": None}
    }

    # Environments of api
    PORT = __all_environments[__env]["port"]
    HOST = __all_environments[__env]["host"]
    DEBUG = __all_environments[__env]["debug"]
    SWAGGER_URL = __all_environments[__env]["swagger-url"]

    # Databases connection
    NEO4J_URL = os.environ.get("NEO4J_URL") + "/db/data/"
    NEO4J_IP = os.environ.get("NEO4J_IP") + " /db/data/"
    NEO4J_USERNAME = "neo4j"
    NEO4J_PWD = "test"
