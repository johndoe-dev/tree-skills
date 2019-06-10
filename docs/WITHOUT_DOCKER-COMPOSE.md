[return to README.md](../README.md)

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

### DOCKER

### Install tree-skills_api

Create image
```
$ docker build -t tree-skills_api .
```
Export your source code into an environment variable
```
$ export MY_SRC_CODE=your-path
```
bind your code into /home/app directory, define  port and workdir
```
$ sudo docker run -dit --name tree-skills_api -p 5000:5000 -p 59153:59153 -v $MY_SRC_CODE:/home/app -w /home/app tree-skills_api:latest
```
Create an alias to execute command inside your container (optional)
```
$ alias api='sudo docker exec -it tree-skills_api'
```

### Install neo4j
Create database volume
```
$ export NEO4J_DB=your-path
$ mkdir -p $NEO4J_DB/data $NEO4J_VOL/logs
```
Launch this comand (it will pull and start container)
```
$ sudo docker run \
    -dit \
    --name=tree-skills_db \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$NEO4J_DB/data:/data \
    --volume=$NEO4J_DB/logs:/logs \
    neo4j:3.0
```
Create test database volume
```
$ export NEO4J_TEST=your-path
$ mkdir -p $NEO4J_TEST/data $NEO4J_VOL/logs
```
```
$ sudo docker run \
    -dit \
    --name=tree-skills_testdb \
    --publish=7475:7474 --publish=7688:7687 \
    --volume=$NEO4J_TEST/data:/data \
    --volume=$NEO4J_TEST/logs:/logs \
    neo4j:3.0
```

### Link containers
Create a network bridge
```
$ docker network create tree-skills_bridge
```

Connect each container into the bridge and create a link
```
$ docker network connect tree-skills_bridge tree-skills_api --link tree-skills_db --link tree-skills_testdb
```
```
$ docker network connect tree-skills_bridge tree-skills_db
```
```
$ docker network connect tree-skills_bridge tree-skills_testdb
```

If you use a different name for databases container, change value in **.env**
```
NEO4J_DATABASE_URL=http://tree-skills_db:7474
NEO4J_DATABASE_URL_TEST=http://tree-skills_testdb:7474
```

Pay attention to the format: http://{container_name}:{port}

### Define neo4js password

On browser, go to http://localhost:7474 for **db** and http://localhost:7474 for **test_db**

Define password for each database

In src/environment/instance, Change value of **NEO4J_DATABASE_PWD** (Default is "test")  
The same password is used for db and test_db



# RUN
To create Database
```
$ api python main.py create_all
```
To delete Database
```
$ api python main.py delete_all
```
To run tests
```
$ api python src/main.py test
```
To tail
```
$ docker logs --follow tree-skills_api
```

open http://localhost:5000/api/1/ in browser
