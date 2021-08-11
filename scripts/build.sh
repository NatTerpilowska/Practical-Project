#!/bin/bash

docker-compose build --parallel && \
docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}
docker-compose push