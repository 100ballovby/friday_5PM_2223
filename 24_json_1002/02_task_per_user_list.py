import json


def json_to_obj(json_file):
    with open(json_file, 'r') as file:
        data = json.loads(file.read())
    return data


def obj_to_json(obj, json_file):
    with open(json_file, 'w') as file:
        file.write(json.dumps(obj, indent=4))


todos = json_to_obj("todos.json")
users = json_to_obj("users.json")

usernames = {}
for user in users:
    usernames[user["id"]] = user["name"]

# второй вариант решения (через список)
users_tasks_list = {}
for task in todos:
    id = task["userId"]
    name = usernames[id]
    if task["completed"]:  # если задача выполнена
        if name not in users_tasks_list:
            users_tasks_list[name] = [1, 0]
        else:
            users_tasks_list[name][0] += 1
    if not task["completed"]:  # если задача выполнена
        if name not in users_tasks_list:
            users_tasks_list[name] = [0, 1]
        else:
            users_tasks_list[name][1] += 1

for user in users_tasks_list.keys():
    print(f"User: {user};")
    print(f"Completed: {users_tasks_list[user][0]} tasks;")
    print(f"Didn't completed: {users_tasks_list[user][1]} tasks;")
    print()