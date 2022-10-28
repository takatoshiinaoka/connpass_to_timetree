import requests
import json
import os
from dotenv import load_dotenv
load_dotenv('./.env')

TOKEN = os.environ.get('TIMETREE_TOKEN')
TIMETREE_BASEURL = os.environ.get('TIMETREE_BASEURL')
CALENDAR_ID = os.environ.get('CALENDAR_ID')

# Json読み込み
json_open = open('./events.json', 'r')
json = json.load(json_open)

# Connpassからイベント取得
nickname = os.environ.get('NICKNAME')
responce = requests.get(f"https://connpass.com/api/v1/event/?count=100&nickname={nickname}").json()
events = responce["events"]

# JsonのイベントIDとConnpassのイベントIDを取得
jsonArray = []
connpassArray = []
for event in json:
    jsonArray.append(event["event_id"])
for event in events:
    connpassArray.append(event["event_id"])

# JsonとConnpassのイベントの差分を取得
diff_id = set(connpassArray) ^ set(jsonArray) 
# print("diff:",diff_id) # 新しく登録したイベント

# TimeTreeに登録する関数
def post_timetree(event):
    # print("Hello",event["event_id"])
    headers = {'Authorization': f"Bearer {TOKEN}"}
    data = {
        "data": {
            "attributes": {
                "category": "schedule",
                "title": event["title"],
                "all_day": "false",
                "start_at": event["started_at"],
                "start_timezone": "UTC",
                "end_at": event["ended_at"],
                "end_timezone": "UTC",
                "description": "",
                "location":event["place"],
                "url": event["event_url"]
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
    result = requests.post(f"{TIMETREE_BASEURL}/calendars/{CALENDAR_ID}/events/", json=data, headers=headers)
    print(result.json())

# 新しいイベントをTimeTreeに登録
for id in diff_id:
    for event in events:
        if(event["event_id"] == id):
            post_timetree(event)









