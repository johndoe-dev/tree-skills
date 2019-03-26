from flask_restplus import Namespace, Resource, fields
from models.person import person
from database.neo4j import graph
import json
from json import dumps


ns = Namespace('persons', description='Persons related operations')


@ns.route('/')
class PersonList(Resource):
    @ns.marshal_list_with(person)
    def get(self):
        result = dumps(graph.run('MATCH (book:Book) RETURN book').data())
        r = json.loads(result)
        print(r[0]["book"])
        # return [serialize_genre(record['genre']) for record in result]
        return r[0]["book"]

    @ns.expect(person, validate=True)
    @ns.marshal_with(person)
    def post(self):
        new_book = ns.payload["title"]
        query = "CREATE({0}: Book {{title: {0}}})".format(new_book)
        result = dumps(graph.run("CREATE({0}: Book {{title: '{0}'}})".format(new_book)).data())
        return result
