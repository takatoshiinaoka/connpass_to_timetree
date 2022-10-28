from dataclasses import dataclass
import requests
import json
import datetime
import os
from dotenv import load_dotenv
load_dotenv('./.env')

json_open = open('./test.json', 'r')
json_load = json.load(json_open)
TOKEN = os.environ.get('TIMETREE_TOKEN')
TIMETREE_BASEURL = os.environ.get('TIMETREE_BASEURL')
CALENDAR_ID = os.environ.get('CALENDAR_ID')
today = datetime.date.today()

headers = {'Authorization': f"Bearer {TOKEN}"}
data = {
    "data": {
        "attributes": {
            "category": "schedule",
            "title": "これはテストです😊",
            "all_day": "false",
            "start_at": f"{today}T00:00:00.000Z",
            "start_timezone": "UTC",
            "end_at": f"{today}T12:00:00.000Z",
            "end_timezone": "UTC",
            "description": "",
            "location": "オンライン(YouTube)",
            "url": "https://github.com"
        },
        "relationships": {
            "label": {
                "data": {
                    "id": "${calendar_id},2", 
                    "type": "label"
                }
            }
        }
    }
}

private = requests.post(f"{TIMETREE_BASEURL}/calendars/{CALENDAR_ID}/events/", json=data, headers=headers)
print(private.json())
