from flask_restplus import Namespace, Resource, fields
from models.book import book
from database.neo4j import graph
import json
from json import dumps


ns = Namespace('books', description='Books related operations')

# # Let's just keep them in memory
# books_db = [
#     {"id": 0, "title": "War and Peace"},
#     {"id": 1, "title": "Python for Dummies"},
# ]
#
# # This class will handle GET and POST to /books
# @ns.route('/')
# class BookList(Resource):
#     @ns.marshal_list_with(book)
#     def get(self):
#         return books_db
#
#     # Ask flask_restplus to validate the incoming payload
#     @ns.expect(book, validate=True)
#     @ns.marshal_with(book)
#     def post(self):
#         # Generate new Id
#         ns.payload["id"] = books_db[-1]["id"] + 1 if len(books_db) > 0 else 0
#         books_db.append(ns.payload)
#         return ns.payload
#
#
# # Handles GET and PUT to /books/:id
# # The path parameter will be supplied as a parameter to every method
# @ns.route('/<int:id>')
# class Book(Resource):
#     # Utility method
#     def find_one(self, id):
#         return next((b for b in books_db if b["id"] == id), None)
#
#     @ns.marshal_with(book)
#     def get(self, id):
#         match = self.find_one(id)
#         return match if match else ("Not found", 404)
#
#     @ns.marshal_with(book)
#     def delete(self, id):
#         global books_db
#         match = self.find_one(id)
#         books_db = list(filter(lambda b: b["id"] != id, books_db))
#         return match
#
#     # Ask flask_restplus to validate the incoming payload
#     @ns.expect(book, validate=True)
#     @ns.marshal_with(book)
#     def put(self, id):
#         match = self.find_one(id)
#         if match != None:
#             match.update(ns.payload)
#             match["id"] = id
#         return match


@ns.route('/')
class BookList(Resource):
    @ns.marshal_list_with(book)
    def get(self):
        result = dumps(graph.run('MATCH (book:Book) RETURN book').data())
        r = json.loads(result)
        print(r[0]["book"])
        # return [serialize_genre(record['genre']) for record in result]
        return r[0]["book"]

    @ns.expect(book, validate=True)
    @ns.marshal_with(book)
    def post(self):
        new_book = ns.payload["title"]
        query = "CREATE({0}: Book {{title: {0}}})".format(new_book)
        result = dumps(graph.run("CREATE({0}: Book {{title: '{0}'}})".format(new_book)).data())
        return result
