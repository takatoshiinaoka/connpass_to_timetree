# from email import header
# from unittest import result
from dataclasses import dataclass
import requests
import json
import urllib.parse

import os
from dotenv import load_dotenv
load_dotenv('./.env')


TOKEN = os.environ.get('TIMETREE_TOKEN')
TIMETREE_BASEURL = os.environ.get('TIMETREE_BASEURL')

headers = {'Authorization': f"Bearer {TOKEN}"}
data = {
    "data": {
        "attributes": {
            "category": "schedule",
            "title": "これはテストです😊",
            "all_day": "false",
            "start_at": "2022-10-20T00:00:00.000Z",
            "start_timezone": "UTC",
            "end_at": "2022-10-20T06:00:00.000Z",
            "end_timezone": "UTC",
            "description": "これはテストです",
            "url": "https://example.com"
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



private = requests.post("https://timetreeapis.com/calendars/3Lx05Ua8aDVY/events/", json=data, headers=headers)
print(private.json())


