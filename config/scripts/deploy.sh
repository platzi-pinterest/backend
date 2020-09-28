#!/bin/bash

# Use: sh deploy.sh
# Flags: sh deploy.sh update/clean/migrate

# Config elements
PROJECT='eventup'
COMMAND=$1

BASE_NAME=$(basename $0)
BASE_PATH=$(dirname $(readlink -f $0))
BASE_PATH_NAME="$BASE_PATH/$BASE_NAME"

echo "Script path with name: $BASE_PATH_NAME"

# Inside the project
FILE_DOCKER=production.yml
COMPOSE_FILE="$BASE_PATH/$FILE_DOCKER"
export COMPOSE_FILE=$COMPOSE_FILE

# Flag Ubuntu
FILE_DOCKER_COMPOSE="$BASE_PATH/docker-compose.yml"
sudo rm -rf $FILE_DOCKER_COMPOSE
sudo cp $COMPOSE_FILE $FILE_DOCKER_COMPOSE

# Stop Services
sudo supervisorctl stop $PROJECT
sudo docker-compose down

# Remove all
if [ "$COMMAND" = 'clean' ]; then
sudo docker rm -vf $(sudo docker ps -a -q)
sudo docker rmi -f $(sudo docker images -a -q)
sudo docker system prune -f
sudo docker volume prune -f
fi

# Get new changes &&  Build new changes Get Pull
# git clean
git reset --hard
git checkout master
git reset --hard origin/master
git fetch --all
git pull origin master | sudo docker-compose build

# Migrations
if [  "$COMMAND" = 'clean' || "$COMMAND" = 'migrate' ]; then
sudo find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
sudo find . -path "*/migrations/*.pyc" -delete
sudo docker-compose run --rm django python manage.py makemigrations
sudo docker-compose run --rm django python manage.py migrate
fi

# Up new services and Active auto services
sudo docker-compose up --force-recreate -d && sudo supervisorctl start $PROJECT && sudo supervisorctl restart all
