import unittest
from src.tests.base import BaseTestCase


class TestTechnoModel(BaseTestCase):

    def test_get(self):
        techs = self.techno.lists
        self.assertTrue(techs != [])

        neo4j = self.techno.get(name="Neo4j")
        self.assertTrue(neo4j.name == "Neo4j")

    def test_post(self):
        self.techno.post({"name": "New techno"})
        new_techno = self.techno.get(name="New techno")
        self.assertTrue(new_techno.name == "New techno")

    def test_put(self):
        self.techno.put("Neo4j", {"name": "New name"})
        neo4j = self.techno.get(name="New name")
        self.assertTrue(neo4j.name == "New name")

    def test_delete(self):
        self.techno.delete("Python")
        python = self.team.get(name="Python")
        self.assertTrue(python is None)

    def test_relation(self):
        neo4j = self.techno.relation(rel="persons", name="Neo4j", target="person")[0]
        self.assertTrue(neo4j["person"] != [])


if __name__ == '__main__':
    unittest.main()
