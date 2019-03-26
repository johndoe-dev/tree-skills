from flask_restplus import fields
from server.instance import server

techno = server.api.model('Techno', {
    'type': fields.String(required=True, min_length=1, max_length=200, description='Person name'),

})
#
# // Create
# technology
# node
# CREATE(Neo4j: Database
# {techno: 'Neo4j', type: 'NoSQL GraphDB'})
# CREATE(VueJS: Framework
# {techno: 'VueJS', type: 'Frontend JS Framework'})
# CREATE(Javascript: Language
# {techno: 'Javascript', type: 'Imperatif Interpreted Object Language'})
# CREATE(Typescript: Language
# {techno: 'Typescript', type: 'Imperatif Transpilable Typed Object Language'})
# CREATE(D3JS: Library
# {techno: 'D3JS', type: 'Javascript Library'})
# CREATE(Python: Language
# {techno: 'Python', type: 'Imperatif interprated structured language'})
# CREATE(Flask: Framework
# {techno: 'Flask', type: 'MVC Web Framework'})
# // Create
# person
# node
# CREATE(Raphael: Person
# {name: 'Raphaël CHIR'})
# CREATE(Hatim: Person
# {name: 'Hatim Heffoudhi'})
# CREATE(Jonathan: Person
# {name: 'Jonathan Ullindah'})
# // Create
# team
# node
# CREATE(R1: Team
# {name: 'R1', type: 'Business Unit', tagline: 'Centre de production IDF'})
# CREATE(R6: Team
# {name: 'R6', type: 'Business Unit', tagline: 'Squads'})
# CREATE(NEXSIS: Team
# {name: 'Nexsis SGA', type: 'Project'})
# CREATE(OFII: Team
# {name: 'Ofii DNA', type: 'Project'})
# // Create
# relations
# CREATE
# (Raphael) - [: JAM_WITH
# {rate: 9}]->(Neo4j),
# (Hatim) - [: JAM_WITH
# {rate: 9}]->(Neo4j),
# (Jonathan) - [: JAM_WITH
# {rate: 9}]->(Neo4j),
# (Raphael) - [: JAM_WITH
# {rate: 5}]->(VueJS),
# (Hatim) - [: JAM_WITH
# {rate: 12}]->(Python),
# (Jonathan) - [: JAM_WITH
# {rate: 15}]->(Python),
# (Jonathan) - [: JAM_WITH
# {rate: 14}]->(Flask),
# (Hatim) - [: JAM_WITH
# {rate: 14}]->(Typescript),
# (Raphael) - [: JAM_WITH
# {rate: 12}]->(Javascript),
# (Raphael) - [: PLAYED_IN]->(R6),
# (Raphael) - [: PLAYED_IN]->(NEXSIS),
# (Raphael) - [: PLAYED_IN]->(OFII),
# (Raphael) - [: PLAYED_IN]->(R1),
# (Hatim) - [: PLAYED_IN]->(NEXSIS),
# (Hatim) - [: PLAYED_IN]->(OFII),
# (Hatim) - [: PLAYED_IN]->(R1),
# (Hatim) - [: PLAYED_IN]->(R6),
# (Jonathan) - [: PLAYED_IN]->(R6)
# // Launch
# a
# find
# request
# WITH
# Neo4j as tek
# MATCH(tek) < -[: JAM_WITH]-(user) - [: PLAYED_IN]->(team)
# RETURN
# tek, user, team
# LIMIT
# 10
# ;


