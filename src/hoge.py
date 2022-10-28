import requests
import json

json_open = open('./events.json', 'r')
json_load = json.load(json_open)

jsonArray = []
for event in json_load:
    jsonArray.append(event["event_id"])

# print(jsonArray)


responce = requests.get("https://connpass.com/api/v1/event/?count=100&nickname=inaoka01").json()
events = responce["events"]

connpassArray = []
for event in events:
    connpassArray.append(event["event_id"])

# print(jsonArray)
# print(connpassArray)
diff_id = set(connpassArray) ^ set(jsonArray) 
print(diff_id)

def post_timetree(event):
    print("Hello")
    path = './test.json'
    json_file = open(path, mode="w")
    json.dump(event, json_file, ensure_ascii=False)
    json_file.close()

for id in diff_id:
    for event in events:
        if(event["event_id"] == id):
            post_timetree(event)

# print(json_load)

