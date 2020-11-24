import json


def count_user(work_json):
    user_count = []
    for i in work_json:
        change = True
        for j in range(len(user_count)):
            if user_count[j] == i['userId']:
                change = False
        if change:
            user_count.append(i['userId'])
    return len(user_count)


with open("save_from_server.json", "r") as json_file:
    work_json = json.load(json_file)
print(count_user(work_json))
