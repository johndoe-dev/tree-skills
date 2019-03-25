import os
from dotenv import load_dotenv


basedir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../../.env"))
load_dotenv(basedir)


# # Load the development "mode". Use "development" if not specified
# env = os.environ.get("PYTHON_ENV", "development")
#
# # Configuration for each environment
# # Alternatively use "python-dotenv"
# all_environments = {
#     "development": { "port": 5000, "host": "0.0.0.0", "debug": True, "swagger-url": "/" },
#     "production": { "port": 8080, "host": "0.0.0.0", "debug": False, "swagger-url": None  }
# }
#
# # The config for the current environment
# # environment_config = all_environments[env]
# config = {
#     "environment_config": all_environments[env],
#     "database": {
#         "url": os.environ.get("URL")
#     }
# }

class Config(object):
    __env = os.environ.get("PYTHON_ENV", "development")

    __all_environments = {
        "development": {"port": 5000, "host": "0.0.0.0", "debug": True, "swagger-url": "/"},
        "production": {"port": 8080, "host": "0.0.0.0", "debug": False, "swagger-url": None}
    }

    PORT = __all_environments[__env]["port"]
    HOST = __all_environments[__env]["host"]
    DEBUG = __all_environments[__env]["debug"]
    SWAGGER_URL = __all_environments[__env]["swagger-url"]
    NEO4J_URL = os.environ.get("NEO4J_URL")