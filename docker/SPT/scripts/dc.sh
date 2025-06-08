#!/bin/bash

BASE_DIR=</path/to/EFT/scripts>
DOCKER_COMPOSE_FILE=$BASE_DIR/docker-compose.yml
DOCKER_COMPOSE="docker compose"
cd $BASE_DIR
$DOCKER_COMPOSE -f $DOCKER_COMPOSE_FILE $@