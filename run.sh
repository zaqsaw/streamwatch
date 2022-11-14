#!/bin/bash

mount=$1
DOCKER_CONTAINER=$(docker run --volume ${mount}:/app/download -d streamwatcher:latest)
docker cp docker/app/config.ini ${DOCKER_CONTAINER}:/app/config.ini
docker logs -f ${DOCKER_CONTAINER}

