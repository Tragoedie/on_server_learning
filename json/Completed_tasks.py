import json


def completed_task(work_json):
    user = {}
    for i in work_json:
        user[i["userId"]] = {"num": 0, "completed": 0}
    for j in work_json:
        user[j["userId"]]["num"] += 1
        if j['completed'] is True:
            user[j["userId"]]["completed"] += 1
    return user


def completed_task_1(work_json):
    user_1 = {}
    for i in range(len(work_json)):
        user_1[work_json[i]["userId"]] = {"num": 0, "completed": 0}
    for j in range(len(work_json)):
        user_1[work_json[j]["userId"]]["num"] += 1
        if work_json[j]["completed"] is True:
            user_1[work_json[j]["userId"]]["completed"] += 1
    return user_1


with open("save_from_server.json", "r") as json_file:
    work_json = json.load(json_file)

print(completed_task(work_json))
print(completed_task_1(work_json))

