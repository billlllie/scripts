#!/bin/bash

set -e
BASE_PATH=/app/server
DATA_PATH=$BASE_PATH/bin/SPT_Data
BACKUP_DATA_PATH=$BASE_PATH/backup/SPT_Data
BIN_PATH=$BASE_PATH/bin
SERVER=$BIN_PATH/SPT.Server.exe

if ([ "$(ls -A $DATA_PATH)" ]); then
    echo "Directory is not empty."
else
    echo "Directory is empty. Copy SPT_Data folder..."
    cp -r $BACKUP_DATA_PATH $BIN_PATH
fi
echo "Change directory to $BIN_PATH"
cd $BIN_PATH
echo "Current directory is $(pwd). Now starting server ..."
$SERVER