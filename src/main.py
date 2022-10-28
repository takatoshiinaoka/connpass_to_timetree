import requests
import json
import sys
# import os
# from dotenv import load_dotenv
# load_dotenv('./.env')
args = sys.argv

# TOKEN = os.environ.get('TIMETREE_TOKEN')
# TIMETREE_BASEURL = os.environ.get('TIMETREE_BASEURL')
# CALENDAR_ID = os.environ.get('CALENDAR_ID')

TOKEN = args[1]
TIMETREE_BASEURL = args[2]
CALENDAR_ID = args[3]
nickname = args[4]

print(TOKEN,TIMETREE_BASEURL,CALENDAR_ID,nickname)

# JsonからTimeTreeに登録済みのイベントID読み込み
json_open = open('./events.json', 'r')
jsonArray = json.load(json_open)

# Connpassからイベント取得
# nickname = os.environ.get('NICKNAME')
responce = requests.get(f"https://connpass.com/api/v1/event/?count=100&nickname={nickname}").json()
events = responce["events"]

# ConnpassのイベントIDを取得
connpassArray = []
for event in events:
    connpassArray.append(event["event_id"])

# JsonとConnpassのイベントの差分を取得
diff_id = set(connpassArray) ^ set(jsonArray) 
# print("diff:",diff_id) # 新しく登録したイベント

# TimeTreeに登録する関数
def post_timetree(event,TIMETREE_BASEURL,CALENDAR_ID):
    print("Hello",event["event_id"])
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
    url = f"{TIMETREE_BASEURL}/calendars/{CALENDAR_ID}/events/"
    print(url)
    result = requests.post(url, json=data, headers=headers)
    print(result.json())

# 新しいイベントをTimeTreeに登録
for id in diff_id:
    for event in events:
        if(event["event_id"] == id):
            post_timetree(event,TIMETREE_BASEURL,CALENDAR_ID)

# TimeTreeに登録したイベントIDの情報を更新
path = './events.json'
json_file = open(path, mode="w")
json.dump(connpassArray, json_file, ensure_ascii=False)
json_file.close()

