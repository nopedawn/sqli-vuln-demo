#!/bin/sh
cd src/

declare NGINX="nginx"
declare MYSQL="mysql"
declare APP="sqli_vuln_demo"

docker compose stop $NGINX $MYSQL $APP
docker compose rm $NGINX $MYSQL $APP
docker rmi $(docker images -q $NGINX) $(docker images -q $MYSQL) $(docker images -q $APP)
