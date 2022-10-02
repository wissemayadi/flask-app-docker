##### Build Docker image from Dockerfile:
```
docker build -t flask-tutorial:latest .
```

##### Create a new container:
```
docker run -d --volume=flask-data:/app/logger  -p 5001:5001 flask-tutorial
```

##### Operate and access Docker container:
```
docker exec -it ca5ef7b23cc3 /bin/sh
```

##### Tag a Docker image:
```
docker tag flask-tutorial:latest radhouenassakra/flask-tutorial:0.1
```
##### Push Docker Image:
```
docker push radhouenassakra/flask-tutorial:0.1
```


##### Create a network:
```
docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 flsk-host-network
```

##### Connect Docker Container to a network:
```
docker network connect --ip 172.20.128.2 flask-host-network eab41a75b2fa```
```
##### Create a Volume:
```
docker volume create flask-data
```

##### Display All volumes:
```
docker volume list
```

##### Attach container to a Volume:
```
docker run -d --volume=flask-data:/app/logger  -p 5001:5001 flask-tutorial
```
##### Inspect Container Volume:
```
docker inspect flask-tutorial-container
```