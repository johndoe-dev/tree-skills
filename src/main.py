# Need to import all resources
# so that they register with the server
from resources.book import ns as book_ns
from resources.person import ns as person_ns
from server.instance import server


def main():
    server.api.add_namespace(book_ns)
    server.api.add_namespace(person_ns)
    server.app.register_blueprint(server.blueprint)
    server.run()


if __name__ == '__main__':
    main()
