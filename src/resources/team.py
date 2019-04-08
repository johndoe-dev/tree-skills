from flask_restplus import Namespace, Resource, abort
from models import PersonModel, TeamModel
from server.instance import server

ns = Namespace("teams", description="Persons related operations", ordered=True)
team = TeamModel(graph=server.graph, api=server.api)
person = PersonModel(graph=server.graph, api=server.api)


@ns.route("/")
class TeamList(Resource):
    @ns.doc("Get all teams")
    @ns.marshal_list_with(team.model("Team"))
    @ns.response(200, "Success")
    def get(self):
        """Get all teams"""
        return team.lists

    @ns.doc("Create one team")
    @ns.expect(team.model("Team"), validate=True)
    @ns.marshal_with(team.model("Team"))
    @ns.response(201, "Created")
    def post(self):
        """Create one team"""
        return team.post(ns.payload), 201


@ns.route("/<string:name>")
class Team(Resource):
    @ns.doc("Get one or more teams by name")
    @ns.marshal_with(team.model("Team"))
    @ns.response(200, "Success")
    @ns.response(404, "Not found")
    def get(self, name):
        """Get one or more teams by name"""
        result = team.get(name, one=False)
        if result:
            return result
        return abort(code=404, message="Team '{}' not found".format(name))

    @ns.doc("Update a team")
    @ns.expect(team.model("Team"))
    @ns.marshal_with(team.model("Team"))
    @ns.response(201, "Team updated")
    @ns.response(404, "Not found")
    def put(self, name):
        """Update a team"""
        result = team.put(name, ns.payload)
        if result:
            return result, 201
        return abort(code=404, message="Team '{}' can't be updated because not found".format(name))

    @ns.doc("Delete a team")
    @ns.marshal_with(team.model("Team"))
    @ns.response(204, "Team deleted")
    @ns.response(404, "Not found")
    def delete(self, name):
        """Delete a team"""
        result = team.delete(name)
        if result:
            return result, 204
        return abort(code=404, message="Team '{}' can't be updated because not found".format(name))


@ns.route("/persons")
class TeamPersonList(Resource):
    @ns.doc("Get all teams related from Person by PLAYED_IN")
    @ns.marshal_list_with(team.model("TeamPerson"))
    @ns.response(200, "Success")
    def get(self):
        """Get all teams related from Person by PLAYED_IN"""
        return team.relation(rel="persons", target="person")


@ns.route("/<string:name>/persons")
class TeamPersonList(Resource):
    @ns.doc("Get one ore more teams related from Person by PLAYED_IN")
    @ns.marshal_list_with(team.model("TeamPerson"))
    @ns.response(200, "Success")
    def get(self, name):
        """Get all teams related from Person by PLAYED_IN"""
        return team.relation(rel="persons", name=name, target="person")

