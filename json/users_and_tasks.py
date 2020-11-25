import json

with open("save_from_server.json", "r") as json_file:
    work_json = json.load(json_file)

user = {}
for i in work_json:
    if user.get(i['userId'], -1) == -1:
        user[i["userId"]] = {"num": 0, "completed": 0}
    user[i["userId"]]["num"] += 1
    if i['completed'] is True:
        user[i["userId"]]["completed"] += 1


print(user)
print(len(user))
