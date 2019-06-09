import unittest
from src.tests.base import BaseTestCase


class TestPersonModel(BaseTestCase):

    def test_get(self):
        persons = self.person.lists
        self.assertTrue(persons != [])

        hatim = self.person.get(name="Hatim Heffoudhi")
        self.assertTrue(hatim.name == "Hatim Heffoudhi")

    def test_post(self):
        self.person.post({"name": "New Person"})
        new_person = self.person.get(name="New Person")
        self.assertTrue(new_person.name == "New Person")

    def test_put(self):
        self.person.put("Hatim Heffoudhi", {"name": "Hatim"})
        hatim = self.person.get(name="Hatim")
        self.assertTrue(hatim.name == "Hatim")

    def test_delete(self):
        self.person.delete("Hatim Heffoudhi")
        hatim = self.person.get(name="Hatim Heffoudhi")
        self.assertTrue(hatim is None)

    def test_relation(self):
        raphael = self.person.relation(rel="JAM_WITH", name="Raphaël CHIR", target="techno")[0]
        self.assertTrue(raphael["techno"] != [])


if __name__ == '__main__':
    unittest.main()
