#!/bin/bash

docker build -t localhost:5000/babeld .
docker push localhost:5000/babeld
