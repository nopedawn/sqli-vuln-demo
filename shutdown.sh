#!/bin/sh
docker compose down
docker image rm $(docker images -aq)