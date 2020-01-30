#!/bin/bash

docker pull nikitach/babeld:latest
docker tag nikitach/babeld:latest localhost:5000/babeld
docker push localhost:5000/babeld

#docker pull registry:2.7.1
#docker tag registry:2.7.1 localhost:5000/registry
#docker push localhost:5000/registry

docker pull dragonflyoss/dfclient:1.0.0
docker tag dragonflyoss/dfclient:1.0.0 localhost:5000/dfclient
docker push localhost:5000/dfclient

docker pull dragonflyoss/supernode:1.0.0
docker tag dragonflyoss/supernode:1.0.0 localhost:5000/supernode
docker push localhost:5000/supernode

docker build -t dragonfly_stage1 .
docker run --privileged -d --name dragonfly_build dragonfly_stage1
sleep 10
docker exec dragonfly_build docker-compose up --no-start
sleep 10
docker stop dragonfly_build
docker commit dragonfly_build dragonfly_dind
docker rm dragonfly_build
echo '***Image dragonfly_dind erstellt!'
