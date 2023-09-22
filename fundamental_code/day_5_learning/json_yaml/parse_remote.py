import urllib.request
import requests
import json

with urllib.request.urlopen("http://jsonplaceholder.typicode.com/todos/1") as url:
    data = json.load(url)
    print(data)

poke_request = requests.get("http://jsonplaceholder.typicode.com/todos/1")
poke_json = poke_request.json()
print(poke_request.keys())
