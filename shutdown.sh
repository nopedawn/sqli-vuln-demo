#!/bin/sh
cd src/
docker compose down
docker image rm $(docker images -aq)