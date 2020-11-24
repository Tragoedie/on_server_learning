import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(response.text)
print(result)

with open("save_from_server.json", "w") as json_file:
    json.dump(result, json_file)
