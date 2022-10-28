#!/bin/bash

source ./.env
echo $TIMETREE_TOKEN 
echo $TIMETREE_BASEURL 
echo $CALENDAR_ID 
echo $NICKNAME 
python src/main.py $TIMETREE_TOKEN $TIMETREE_BASEURL $CALENDAR_ID $NICKNAME 