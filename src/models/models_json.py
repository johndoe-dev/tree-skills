from flask_restplus import fields
from server.instance import server


"""Model use for Person"""
person = server.api.model("Person", {
    "name": fields.String(required=True, min_length=1, max_length=200, description="Person name"),
})

"""Model use for Techno"""
techno = server.api.model("Techno", {
    "name": fields.String(required=True, min_length=1, max_length=200, description="Technology name"),
    "type": fields.String(required=True, min_length=1, max_length=200, description="Technology type"),
    "description": fields.String(required=True, max_length=200, description="Technology description")
})

"""Model use for Team"""
team = server.api.model("Team", {
    "name": fields.String(required=True, min_length=1, max_length=200, description="Technology name"),
    "type": fields.String(required=True, min_length=1, max_length=200, description="Technology type"),
    "tagline": fields.String(required=True, max_length=200, description="Technology description")
})

"""Model use for Person relation PLAYED_IN related to Team"""
person_team_model = server.api.model("PersonTeam", {
    "person": fields.Nested(person),
    "team": fields.List(fields.Nested(team))
})

"""Model use for Team relation persons related from Person"""
team_person_model = server.api.model("TeamPerson", {
    "team": fields.Nested(team),
    "person": fields.List(fields.Nested(person))
})

"""Model use for Person relation JAM_WITH related to Techno"""
person_techno_model = server.api.model("PersonTechno", {
    "person": fields.Nested(person),
    "techno": fields.List(fields.Nested(techno))
})

"""Model use for Techno relation persons related from Person"""
techno_person_model = server.api.model("TechnoPerson", {
    "techno": fields.Nested(techno),
    "person": fields.List(fields.Nested(person))
})




