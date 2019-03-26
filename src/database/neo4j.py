from py2neo import Graph
from environment.instance import Config


config = Config()

try:
    graph = Graph(config.NEO4J_URL, username=config.NEO4J_USERNAME, password=config.NEO4J_PWD)
# Throw a SocketError => Connection refused, we have to use the ip@ of the database container
except Exception:
    graph = Graph("http://{username}:{password}@{ip}"
                  .format(username=config.NEO4J_USERNAME,
                          password=config.NEO4J_PWD,
                          ip=config.NEO4J_IP))
