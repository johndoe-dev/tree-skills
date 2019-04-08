from py2neo import Graph
from errors import *


class Database:
    def __init__(self, app=None):
        self._graph = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        try:
            if (
                    "NEO4J_DATABASE_URL" not in app.config or
                    "NEO4J_DATABASE_IP" not in app.config
            ):
                raise Neo4jUriError

            if (
                    "NEO4J_DATABASE_USERNAME" not in app.config and
                    "NEO4J_DATABASE_PWD" not in app.config
            ):
                raise Neo4jAuthError

            self._graph = Graph("http://{username}:{password}@{ip}"
                                .format(username=app.config["NEO4J_DATABASE_USERNAME"],
                                        password=app.config["NEO4J_DATABASE_PWD"],
                                        ip=app.config["NEO4J_DATABASE_IP"]))
        except Neo4jUriError:
            print("NEO4J_DATABASE_URL or NEO4J_DATABASE_IP is not defined in app.config")
        except Neo4jAuthError:
            print("NEO4J_DATABASE_USERNAME and NEO4J_DATABASE_PWD are not defined in app.config")

    @property
    def graph(self):
        return self._graph

    def create_all(self):
        self.graph.run(
            """
            //Create technology node
            CREATE (Neo4j:Techno {name:'Neo4j', type:'Database', description:'NoSQL GraphDB'})
            CREATE (VueJS:Techno {name:'VueJS', type:'Framework', description:'Frontend JS Framework'})
            CREATE (Javascript:Techno {name:'Javascript', type:'Language', description:'Imperatif Interpreted Object Language'})
            CREATE (Typescript:Techno {name:'Typescript', type:'Language', description:'Imperatif Transpilable Typed Object Language'})
            CREATE (D3JS:Techno {name:'D3JS', type:'Library', description:'Javascript Library' })
            CREATE (Python:Techno {name:'Python', type:'Language', description:'Imperatif interprated structured language' })
            CREATE (Flask:Techno {name:'Flask', type:'Framework', description:'MVC Web Framework' })
            //Create person  node
            CREATE (Raphael:Person {name:'Raphaël CHIR'})
            CREATE (Hatim:Person {name:'Hatim Heffoudhi'})
            CREATE (Jonathan:Person {name:'Jonathan Ullindah'})
            //Create team  node
            CREATE (R1:Team {name:'R1', type:'Business Unit', tagline:'Centre de production IDF'  })
            CREATE (R6:Team {name:'R6', type:'Business Unit', tagline:'Squads' })
            CREATE (NEXSIS:Team {name:'Nexsis SGA', type:'Project'})
            CREATE (OFII:Team {name:'Ofii DNA', type:'Project'})
            //Create relations
            CREATE
              (Raphael)-[:JAM_WITH {rate : 9}]->(Neo4j),
              (Hatim)-[:JAM_WITH {rate : 9}]->(Neo4j),
              (Jonathan)-[:JAM_WITH {rate : 9}]->(Neo4j),
              (Raphael)-[:JAM_WITH {rate : 5}]->(VueJS),
              (Hatim)-[:JAM_WITH {rate : 12}]->(Python),
              (Jonathan)-[:JAM_WITH {rate : 15}]->(Python),
              (Jonathan)-[:JAM_WITH {rate : 14}]->(Flask),
              (Hatim)-[:JAM_WITH {rate : 14}]->(Typescript),
              (Raphael)-[:JAM_WITH {rate : 12}]->(Javascript),
              (Raphael)-[:PLAYED_IN]->(R6),
              (Raphael)-[:PLAYED_IN]->(NEXSIS),
              (Raphael)-[:PLAYED_IN]->(OFII),
              (Raphael)-[:PLAYED_IN]->(R1),
              (Hatim)-[:PLAYED_IN]->(NEXSIS),
              (Hatim)-[:PLAYED_IN]->(OFII),
              (Hatim)-[:PLAYED_IN]->(R1),
              (Hatim)-[:PLAYED_IN]->(R6),
              (Jonathan)-[:PLAYED_IN]->(R6)
            """
        )

    def delete_all(self):
        self.graph.delete_all()
