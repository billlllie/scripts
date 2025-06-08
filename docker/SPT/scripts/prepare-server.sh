#!/bin/bash

BASE_DIR=</path/to/EFT>
SERVER_REPO_DIR=server
set -e
cd $BASE_DIR
if [ "$(ls -A $BASE_DIR/$SERVER_REPO_DIR)" ]; then
    echo "Repo already exists."
else
    echo "Repo does not exists. Pulling"
    git clone https://github.com/sp-tarkov/server.git
fi
git fetch origin master
git lfs pull
git reset --hard origin/master