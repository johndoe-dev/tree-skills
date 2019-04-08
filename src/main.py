import unittest
from resources import person_ns, techno_ns, team_ns
from server.instance import server


@server.manager.command
def run():
    server.add_namespaces(person_ns, techno_ns, team_ns)
    server.run()


@server.manager.command
def create_all():
    server.database.create_all()


@server.manager.command
def delete_all():
    server.database.delete_all()


@server.manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('src/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    server.manager.run()