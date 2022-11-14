#!/bin/bash

mount=$1
if [ ! -d "${mount}" ]; then
    echo "${mount} not found, must pass an existing directory"
    exit 1
fi

DOCKER_CONTAINER=$(docker run --volume ${mount}:/app/download -d streamwatcher:latest)
docker cp docker/app/config.ini ${DOCKER_CONTAINER}:/app/config.ini
docker logs -f ${DOCKER_CONTAINER}

