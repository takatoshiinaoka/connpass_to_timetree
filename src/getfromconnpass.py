import requests
import json

responce = requests.get("https://connpass.com/api/v1/event/?count=100&nickname=inaoka01").json()
events = responce["events"]

print("results_start:", responce["results_start"])
print("results_returned", responce["results_returned"])
print("results_available:", responce["results_available"])
print("events length:",len(events))

print(events)
# for i,event in events:
#     print(i,event["title"])

path = './events.json'
json_file = open(path, mode="w")
json.dump(events, json_file, ensure_ascii=False)
json_file.close()