from flask_restplus import Namespace, Resource, fields
from models.person import person
from database.neo4j import graph
from utils.functions import graph_to_json


ns = Namespace('persons', description='Persons related operations')


@ns.route('/')
class PersonList(Resource):
    @ns.marshal_list_with(person)
    def get(self):
        query = 'MATCH (node:Person) RETURN node'
        result = graph.run(query).data()
        return graph_to_json(result, "node")

    @ns.expect(person, validate=True)
    @ns.marshal_with(person)
    def post(self):
        new_person = ns.payload["name"]
        create_query = "CREATE({0}: Person {{name: '{0}'}})".format(new_person)
        graph.run(create_query).data()
        get_query = "MATCH (node:Person) WHERE node.name='{name}' RETURN node LIMIT 1".format(name=new_person)
        get = graph.run(get_query).data()
        return graph_to_json(get, "node")
