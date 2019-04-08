import unittest
from tests.base import BaseTestCase


class TestTeamModel(BaseTestCase):

    def test_get(self):
        teams = self.team.lists
        self.assertTrue(teams != [])

        r1 = self.team.get(name="R1")
        self.assertTrue(r1.name == "R1")

    def test_post(self):
        self.team.post({"name": "New Team"})
        new_team = self.team.get(name="New Team")
        self.assertTrue(new_team.name == "New Team")

    def test_put(self):
        self.team.put("R1", {"name": "New name"})
        r1 = self.team.get(name="New name")
        self.assertTrue(r1.name == "New name")

    def test_relation(self):
        r1 = self.team.relation(rel="persons", name="R1", target="person")[0]
        self.assertTrue(r1["person"] != [])


if __name__ == '__main__':
    unittest.main()
