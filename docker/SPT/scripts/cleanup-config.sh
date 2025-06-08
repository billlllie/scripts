#!/bin/bash

set -e
BASE_PATH=~/opt/games/EFT
REMOVE="rm -r"

$REMOVE $BASE_PATH/config/user/*
$REMOVE $BASE_PATH/config/SPT_Data/*