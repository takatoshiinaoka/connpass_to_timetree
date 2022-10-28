# from email import header
# from unittest import result
from dataclasses import dataclass
import requests
import json

import os
from dotenv import load_dotenv
load_dotenv('./.env')


'''
# requestsのパラメータ指定
url = 'https://www.google.co.jp/search'
params = {'q': '日本代表', 'tbm': 'nws'}
r = requests.get(url, params=params)
print(r.url)
'''


TOKEN = os.environ.get('TIMETREE_TOKEN')
TIMETREE_BASEURL = os.environ.get('TIMETREE_BASEURL')
CALENDAR_ID = "3Lx05Ua8aDVY"

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



private = requests.post(f"{TIMETREE_BASEURL}/calendars/{CALENDAR_ID}/events/", json=data, headers=headers)
print(private.json())

# print(f"{TIMETREE_BASEURL}/calendars/{CALENDAR_ID}/events/")


