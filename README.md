# Tree-skills Api
Backend with database Neo4j
# Development installation
We use:  
py2neo  https://py2neo.org/v3/  
Flask  http://flask.pocoo.org  
flask-restplus  https://flask-restplus.readthedocs.io/en/stable/  
Flask-Script  https://flask-script.readthedocs.io/en/latest/  
Flask-Testing  https://pythonhosted.org/Flask-Testing/  
python-dotenv  https://github.com/theskumar/python-dotenv  
docker https://www.docker.com  
docker-compose https://docs.docker.com/compose/


## INSTALLATION

```
$ git clone https://github.com/johndoe-dev/tree-skills.git
```

or 

```
$ git clone https://gitlab.boost.open.global/open/squads/squad-new-dev/workshops/skills-mapping/tree-skills.git
```
```
$ cd your-project
```

### DOCKER-COMPOSE

#### Install api and databases

This command will the images, the containers and run the server
```
$ docker-compose up --build
```

Image built:  
+ tree-skills_api

Containers created:
+ tree-skills_api
+ tree-skills_db
+ tree-skills_testdb

Network created:
+ tree-skills_default

#### Define neo4js password

On browser, go to http://localhost:7474 for **db** and http://localhost:7474 for **test_db**

Define password for each database

In src/environment/instance, Change value of **NEO4J_DATABASE_PWD** (Default is "test")  
The same password is used for db and test_db


If you don't use "test" for db's password, you must rebuild:

type ctrl+C to stop server, then:

```
$ docker-compose up --build
```

[Install without docker-compose](docs/WITHOUT_DOCKER-COMPOSE.md)

# RUN

**All this command must be run in another terminal**

You can define an alias for your api:
```
$ alias api='sudo docker exec -it tree-skills_api'
```
To create database
```
$ api python main.py create_all
```
To delete Database
```
$ api python main.py delete_all
```
To run tests
```
$ api python main.py test
```

open http://localhost:5000/api/1/ in browser
