from dataclasses import dataclass
import requests
import json

import os
from dotenv import load_dotenv
load_dotenv('./.env')

json_open = open('./test.json', 'r')
json_load = json.load(json_open)
TOKEN = os.environ.get('TIMETREE_TOKEN')
TIMETREE_BASEURL = os.environ.get('TIMETREE_BASEURL')
CALENDAR_ID = os.environ.get('CALENDAR_ID')

headers = {'Authorization': f"Bearer {TOKEN}"}
data = {
    "data": {
        "attributes": {
            "category": "schedule",
            "title": json_load["title"],
            "all_day": "false",
            "start_at": json_load["started_at"],
            "start_timezone": "UTC",
            "end_at": json_load["ended_at"],
            "end_timezone": "UTC",
            "description": json_load["description"],
            "location":json_load["place"],
            "url": json_load["event_url"]
        },
        "relationships": {
            "label": {
                "data": {
                    "id": "${calendar_id},5", 
                    "type": "label"
                }
            }
        }
    }
}

private = requests.post(f"{TIMETREE_BASEURL}/calendars/{CALENDAR_ID}/events/", json=data, headers=headers)
print(private.json())
