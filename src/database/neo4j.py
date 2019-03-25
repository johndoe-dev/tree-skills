from py2neo import Graph, Node, Relationship
from environment.instance import Config


config = Config()

url = "http://127.0.0.1:7474" #config.NEO4J_URL
username = "neo4j"
password = "test"

# http://neo4j:mypassword@1.2.3.4:7474/db/data/


graph = Graph(url + '/db/data/', username=username, password=password)