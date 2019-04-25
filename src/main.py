import unittest
from resources import person_ns, techno_ns, team_ns
from models import PersonModel, TechnoModel, TeamModel
from server.instance import server


@server.manager.command
def run():
    server.add_namespaces(person_ns, techno_ns, team_ns)
    server.run()


@server.manager.command
def create_all():
    person = PersonModel(server)
    techno = TechnoModel(server)
    team = TeamModel(server)

    """Create persons"""
    list_persons = [{"name": "Raphaël CHIR"}, {"name": "Hatim Heffoudhi"}, {"name": "Jonathan Ullindah"}]
    for p in list_persons:
        person.post(p)

    """Create techs"""
    list_techs = [
        {"name": "Neo4j", "type": "Database", "description": "NoSQL GraphDB"},
        {"name": "VueJS", "type": "Framework", "description": "Frontend JS Framework"},
        {"name": "Javascript", "type": "Language", "description": "Imperatif Interpreted Object Language"},
        {"name": "Typescript", "type": "Language", "description": "Imperatif Transpilable Typed Object Language"},
        {"name": "D3JS", "type": "Library", "description": "Javascript Library"},
        {"name": "Python", "type": "Language", "description": "Imperatif interprated structured language"},
        {"name": "Flask", "type": "Framework", "description": "MVC Web Framework"}
    ]
    for tech in list_techs:
        techno.post(tech)

    """Create teams"""
    list_teams = [
        {"name": "R1", "type": "Business Unit", "tagline": "Centre de production IDF"},
        {"name": "R6", "type": "Business Unit", "tagline": "Squads"},
        {"name": "Nexsis SGA", "type": "Project"},
        {"name": "Ofii DNA", "type": "Project"}
    ]
    for t in list_teams:
        team.post(t)

    """Create relations"""
    relations = [
        {"rel": "JAM_WITH", "source": "Raphaël CHIR", "target_object": "Neo4j"},
        {"rel": "JAM_WITH", "source": "Hatim Heffoudhi", "target_object": "Neo4j"},
        {"rel": "JAM_WITH", "source": "Jonathan Ullindah", "target_object": "Neo4j"},
        {"rel": "JAM_WITH", "source": "Raphaël CHIR", "target_object": "VueJS"},
        {"rel": "JAM_WITH", "source": "Hatim Heffoudhi", "target_object": "Python"},
        {"rel": "JAM_WITH", "source": "Jonathan Ullindah", "target_object": "Python"},
        {"rel": "JAM_WITH", "source": "Jonathan Ullindah", "target_object": "Flask"},
        {"rel": "JAM_WITH", "source": "Hatim Heffoudhi", "target_object": "Typescript"},
        {"rel": "JAM_WITH", "source": "Raphaël CHIR", "target_object": "Javascript"},
        {"rel": "PLAYED_IN", "source": "Raphaël CHIR", "target_object": "R6"},
        {"rel": "PLAYED_IN", "source": "Raphaël CHIR", "target_object": "Nexsis SGA"},
        {"rel": "PLAYED_IN", "source": "Raphaël CHIR", "target_object": "Ofii DNA"},
        {"rel": "PLAYED_IN", "source": "Raphaël CHIR", "target_object": "R1"},
        {"rel": "PLAYED_IN", "source": "Hatim Heffoudhi", "target_object": "Nexsis SGA"},
        {"rel": "PLAYED_IN", "source": "Hatim Heffoudhi", "target_object": "Ofii DNA"},
        {"rel": "PLAYED_IN", "source": "Hatim Heffoudhi", "target_object": "R1"},
        {"rel": "PLAYED_IN", "source": "Hatim Heffoudhi", "target_object": "R6"},
        {"rel": "PLAYED_IN", "source": "Jonathan Ullindah", "target_object": "R6"}



    ]
    for relation in relations:
        if relation["rel"] == "JAM_WITH":
            target_object = techno.get(relation["target_object"])
        else:
            target_object = team.get(relation["target_object"])
        person.add_relation(rel=relation["rel"], source_name=relation["source"], target_object=target_object)


@server.manager.command
def delete_all():
    server.database.delete_all()


@server.manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("src/tests", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    server.manager.run()