# Flask api
Backend with database Neo4j
# Development installation
We use:  
py2neo  https://py2neo.org/v3/  
Flask  http://flask.pocoo.org  
flask-restplus  https://flask-restplus.readthedocs.io/en/stable/  
Flask-Script  https://flask-script.readthedocs.io/en/latest/  
Flask-Testing  https://pythonhosted.org/Flask-Testing/  
python-dotenv  https://github.com/theskumar/python-dotenv


## INSTALLATION

```
$ git clone https://github.com/johndoe-dev/flask_restplus.git
```

```
$ cd your-project
```

### DOCKER

### Install flask api
Export your source code into an environment variable
```
$ export MY_SRC_CODE=your-path
```
bind your code into /home/app directory, define  port and wordir
```
$ sudo docker run -dit --name flask-api -p 5000:5000 -p 59153:59153 -v $MY_SRC_CODE:/home/app -w /home/app python:3.7.2-alpine
```
install all required modules
```
$ sudo docker exec -it flask-api pip install -r requirements.txt
```
Create an alias to execute command inside your container (optional)
```
$ alias flaska='sudo docker exec -it flask-api'
```

### Install neo4j
Create your volumes  
```
$ export NEO4J_VOL=your-path
$ mkdir -p $NEO4J_VOL/data $NEO4J_VOL/logs
```
Launch this comand (it will pull and start container)
```
$ sudo docker run \
    -dit \
    --name=neo4j \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$NEO4J_VOL/data:/data \
    --volume=$NEO4J_VOL/logs:/logs \
    neo4j:3.0
```
For test
```
$ sudo docker run \
    -dit \
    --name=neo4j-test \
    --publish=7475:7474 --publish=7688:7687 \
    --volume=$NEO4J_VOL/data:/data \
    --volume=$NEO4J_VOL/logs:/logs \
    neo4j:3.0
```

### Link containers
get ip address of __neo4j__ and __neo4j-test__
```
$ docker inspect -f "{{ .NetworkSettings.IPAddress }}" <containerNameOrId>
```
Replace NEO4J_DATABASE_IP and NEO4J_DATABASE_IP_TEST
#### Example:
```
$ docker inspect -f "{{ .NetworkSettings.IPAddress }}" neo4j
172.10.0.1
```
```
$ docker inspect -f "{{ .NetworkSettings.IPAddress }}" neo4j-test
172.10.0.2
```
In __.env__ file:
```
NEO4J_DATABASE_IP=172.10.0.1:7474
NEO4J_DATABASE_IP_TEST=172.10.0.2:7474
```

# RUN
To create Database
```
$ python src/main.py create_all
```
To delete Database
```
$ python src/main.py delete_all
```
To run tests
```
$ python src/main.py test
```
To run server
```
$ python src/main.py run
```

open http://localhost:5000/api/1/ in browser
