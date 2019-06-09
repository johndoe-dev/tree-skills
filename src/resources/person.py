from flask_restplus import Namespace, Resource, abort
from src.models import PersonModel, TechnoModel, TeamModel
from src.server.instance import server


ns = Namespace("persons", description="Persons related operations", ordered=True)
person = PersonModel(server)
techno = TechnoModel(server)
team = TeamModel(server)


@ns.route("/")
class PersonList(Resource):
    @ns.doc("Get all persons")
    @ns.marshal_list_with(person.model("Person"))
    @ns.response(200, "All Persons found")
    def get(self):
        """Get all persons"""
        return person.lists, 200

    @ns.doc("Create one person")
    @ns.expect(person.model("Person"), validate=True)
    @ns.marshal_with(person.model("Person"))
    @ns.response(201, "Person created")
    def post(self):
        """Create one person"""
        return person.post(ns.payload), 201


@ns.route("/<string:name>")
class Person(Resource):
    @ns.doc("Get one or person by name")
    @ns.marshal_with(person.model("Person"))
    @ns.response(200, "One or more person found")
    @ns.response(404, "Not found")
    def get(self, name):
        """Get one or person by name"""
        result = person.get(name, one=False)
        if result:
            return result
        return abort(code=404, message="Person '{}' not found".format(name))

    @ns.doc("Update a person")
    @ns.expect(person.model("Person"))
    @ns.marshal_with(person.model("Person"))
    @ns.response(201, "Person updated")
    @ns.response(404, "Not found")
    def put(self, name):
        """Update a person"""
        result = person.put(name, ns.payload)
        if result:
            return result, 201
        return abort(code=404, message="Person '{}' can't be updated because not found")

    @ns.doc("Delete a person")
    @ns.marshal_with(person.model("Person"))
    @ns.response(204, "Person deleted")
    @ns.response(404, "Not found")
    def delete(self, name):
        """Delete a person"""
        deleted = person.delete(name)
        if deleted:
            return deleted, 204
        return abort(code=404, message="Person '{}' can't be deleted because not found")


@ns.route("/jam_with")
class PersonJamWithList(Resource):
    @ns.doc("Get all persons related to Techno by JAM_WITH")
    @ns.marshal_list_with(person.model("PersonTechno"))
    @ns.response(200, "All Persons related to Techno found")
    # @ns.response(400, "Validation Error")
    def get(self):
        """Get all persons related to techno by JAM_WITH"""
        return person.relation(rel="JAM_WITH", target="techno"), 200


@ns.route("/<string:name>/jam_with")
class PersonJamWith(Resource):
    @ns.doc("Get one or more person(s) by name related to Techno by JAM_WITH")
    @ns.marshal_with(person.model("PersonTechno"))
    @ns.response(200, "Person related to techno found")
    # @ns.response(400, "Validation Error")
    def get(self, name):
        """Get one or more person(s) by name related to Techno by JAM_WITH"""
        return person.relation(rel="JAM_WITH", name=name, target="techno"), 200


@ns.route("/<string:person_name>/jam_with/techno/<string:techno_name>")
class PersonJamWithTechno(Resource):
    @ns.doc("Create relation between person and techno by JAM_WITH")
    @ns.marshal_with(person.model("PersonTechno"))
    @ns.response(201, "Relation jam_with created between Person and techno")
    # @ns.response(400, "Validation Error")
    def post(self, person_name, techno_name):
        """Create relation between person and techno by JAM_WITH"""
        tech = techno.get(techno_name)
        return person.add_relation(source_name=person_name, rel="JAM_WITH", target_object=tech), 201

    @ns.doc("Delete relation between person and techno by JAM_WITH")
    @ns.marshal_with(person.model("PersonTechno"))
    @ns.response(204, "Relation jam_with between Person and Techno deleted")
    # @ns.response(400, "Validation Error")
    def delete(self, person_name, techno_name):
        """Delete relation between person and techno by JAM_WITH"""
        tech = techno.get(techno_name)
        return person.delete_relation(source_name=person_name, rel="JAM_WITH", target_object=tech), 204


@ns.route("/played_in")
class PersonPlayedIn(Resource):
    @ns.doc("Get all persons related to Team by PLAYED_IN")
    @ns.marshal_list_with(person.model("PersonTeam"))
    @ns.response(200, "All Persons related to Techno found")
    # @ns.response(400, "Validation Error")
    def get(self):
        """Get all persons related to Team by PLAYED_IN"""
        return person.relation(rel="PLAYED_IN", target="team"), 200


@ns.route("/<string:name>/played_in")
class PersonPlayedIn(Resource):
    @ns.doc("Get one ore more persons related to Team by PLAYED_IN")
    @ns.marshal_list_with(person.model("PersonTeam"))
    @ns.response(200, "One ore more Peron related to Techno found")
    # @ns.response(400, "Validation Error")
    def get(self, name):
        """Get all persons related to Team by PLAYED_IN"""
        return person.relation(rel="PLAYED_IN", name=name, target="team"), 200


@ns.route("/<string:person_name>/played_in/team/<string:team_name>")
class PersonJamWithTechno(Resource):
    @ns.doc("Create relation between person and team by PLAYED_IN")
    @ns.marshal_with(person.model("PersonTeam"))
    @ns.response(201, "Relation PLAYED_IN created between Person and Team")
    # @ns.response(400, "Validation Error")
    def post(self, person_name, team_name):
        """Create relation between person and team by PLAYED_IN"""
        a_team = team.get(team_name)
        return person.add_relation(source_name=person_name, rel="PLAYED_IN", target_object=a_team), 201

    @ns.doc("Delete relation between person and team by PLAYED_IN")
    @ns.marshal_with(person.model("PersonTeam"))
    @ns.response(204, "Relation PLAYED_IN between Person and Team deleted")
    # @ns.response(400, "Validation Error")
    def delete(self, person_name, team_name):
        """Delete relation between person and team by PLAYED_IN"""
        a_team = team.get(team_name)
        person.delete_relation(source_name=person_name, rel="PLAYED_IN", target_object=a_team), 204
