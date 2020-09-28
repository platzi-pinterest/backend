#!/bin/bash

# Use: sh deploy.sh
# Flags: sh deploy.sh update/clean
ROUTE=/home/ubuntu/backend/config/scripts/
cd $ROUTE
sudo chmod +x ./config.sh
sudo chmod +x ./deploy.sh

# Config elements
COMMAND=$1

BASE_NAME=$(basename $0)
BASE_PATH=$(dirname $(readlink -f $0))
BASE_PATH_NAME="$BASE_PATH/$BASE_NAME"
# echo "Script path with name: $BASE_PATH_NAME"

# Update all
if [ "$COMMAND" = 'update' ]; then
sudo apt-get update -y && sudo apt-get upgrade -y
fi

# Permissions Git
ROUTE=/home/ubuntu/backend/
GIT_FIX="$ROUTE.git/objects"
cd $GIT_FIX
sudo chown -R "${USER:-$(id -un)}" .

# Inside the project
LOCAL_FILE="$BASE_PATH/deploy.sh"
ROUTE_FILE="$ROUTE/deploy.sh"
sudo rm -rf $ROUTE_FILE
sudo cp $LOCAL_FILE $ROUTE_FILE
sudo chmod +x $ROUTE_FILE
cd $ROUTE
sudo sh deploy.sh $COMMAND
