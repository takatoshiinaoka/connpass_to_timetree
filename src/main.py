import requests
import json
import sys
args = sys.argv

TOKEN = args[1]
CALENDAR_ID = args[2]
nickname = args[3]

# JsonからTimeTreeに登録済みのイベントID読み込み
json_file = open('./events.json', 'r')
jsonArray = json.load(json_file)
json_file.close()

# Connpassからイベント取得
responce = requests.get(f"https://connpass.com/api/v1/event/?count=100&nickname={nickname}").json()
events = responce["events"]

# ConnpassのイベントIDを取得
connpassArray = []
for event in events:
    connpassArray.append(event["event_id"])

# JsonとConnpassのイベントの差分を取得
diff_id = set(connpassArray) ^ set(jsonArray) 

# TimeTreeに登録する関数
def post_timetree(event, TIMETREE_BASEURL, CALENDAR_ID):
    print(f"New Event id:'{event['event_id']}', title:'{event['title']}'")
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
                        "id": "${calendar_id},8", 
                        "type": "label"
                    }
                }
            }
        }
    }
    url = f"{TIMETREE_BASEURL}/calendars/{CALENDAR_ID}/events/"
    result = requests.post(url, json=data, headers=headers)
    print(result.json())

# イベントが更新されてない
if(not diff_id):
    sys.exit("The event has not been updated.")  

# 新しいイベントをTimeTreeに登録
TIMETREE_BASEURL = "https://timetreeapis.com"
for id in diff_id:
    for event in events:
        if(event["event_id"] == id):
            post_timetree(event, TIMETREE_BASEURL, CALENDAR_ID)

# TimeTreeに登録したイベントIDの情報を更新
json_file = open('./events.json', mode="w")
json.dump(connpassArray, json_file, ensure_ascii=False)
json_file.close()
