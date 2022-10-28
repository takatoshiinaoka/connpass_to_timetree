#!/bin/bash

echo TIMETREE_TOKEN=${{ secrets.TIMETREE_TOKEN }}"\n"\
TIMETREE_BASEURL=${{ secrets.TIMETREE_BASEURL }}"\n"\
CALENDAR_ID=${{ secrets.CALENDAR_ID }}"\n"\
NICKNAME=${{ secrets.NICKNAME }} >> .env
