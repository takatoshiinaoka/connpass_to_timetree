import requests
import json
import os
from dotenv import load_dotenv
load_dotenv('./.env')

nickname = os.environ.get('NICKNAME')
responce = requests.get(f"https://connpass.com/api/v1/event/?count=100&nickname={nickname}").json()
events = responce["events"]

print("results_start:", responce["results_start"])
print("results_returned", responce["results_returned"])
print("results_available:", responce["results_available"])
print("events length:",len(events))
# print(events)

event_id = []
for event in events:
    event_id.append(event["event_id"])

path = './events.json'
json_file = open(path, mode="w")
json.dump(event_id, json_file, ensure_ascii=False)
json_file.close()
