from flask_restplus import Namespace, Resource, abort
from models import PersonModel, TechnoModel
from server.instance import server

ns = Namespace("techs", description="Techno related operations", ordered=True)
techno = TechnoModel(graph=server.graph, api=server.api)
person = PersonModel(graph=server.graph, api=server.api)


@ns.route("/")
class TechnoList(Resource):
    @ns.doc("Get all techs")
    @ns.marshal_list_with(techno.model("Techno"))
    @ns.response(200, "Success")
    def get(self):
        """Get all techs"""
        return techno.lists

    @ns.doc("Create one techno")
    @ns.expect(techno.model("Techno"), validate=True)
    @ns.marshal_with(techno.model("Techno"))
    @ns.response(201, "Created")
    def post(self):
        """Create one techno"""
        return techno.post(ns.payload)


@ns.route("/<string:name>")
class Techno(Resource):
    @ns.doc("Get one or more techs by name")
    @ns.marshal_with(techno.model("Techno"))
    @ns.response(200, "Success")
    @ns.response(404, "Not found")
    def get(self, name):
        """Get one or more techs by name"""
        result = techno.get(name, one=False)
        if result:
            return result, 200
        return abort(code=404, message="Techno '{}' not found".format(name))

    @ns.doc("Update a techno")
    @ns.expect(techno.model("Techno"))
    @ns.marshal_with(techno.model("Techno"))
    @ns.response(201, "Techno updated")
    @ns.response(400, "Validation Error")
    def put(self, name):
        """Update a techno"""
        result = techno.put(name, ns.payload)
        if result:
            return result, 201
        return abort(code=404, message="Techno '{}' can't be updated because not found".format(name))

    @ns.doc("Delete a techno")
    @ns.marshal_with(techno.model("Techno"))
    @ns.response(204, "Techno deleted")
    @ns.response(400, "Validation Error")
    def delete(self, name):
        """Delete a techno"""
        result = techno.delete(name)
        if result:
            return result, 204
        return abort(code=404, message="Techno '{}' can't be deleted because not found".format(name))


@ns.route("/persons")
class TechnoPersonList(Resource):
    @ns.doc("Get all Techno related from Person by JAM_WITH")
    @ns.marshal_list_with(techno.model("TechnoPerson"))
    @ns.response(200, "Success")
    def get(self):
        """Get all persons related to techno by JAM_WITH"""
        return techno.relation(rel="persons", target="person"), 200


@ns.route("/<string:name>/persons")
class TechnoPersonList(Resource):
    @ns.doc("Get one or more Techno related from person by JAM_WITH")
    @ns.marshal_list_with(techno.model("TechnoPerson"))
    @ns.response(200, "Success")
    def get(self, name):
        """Get one or more Techno related from person by JAM_WITH"""
        return techno.relation(rel="persons", name=name, target="person"), 200

