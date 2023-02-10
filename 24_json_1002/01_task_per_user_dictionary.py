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

# первый вариант решения (через словарь)
users_tasks = {}
for task in todos:
    id = task["userId"]
    name = usernames[id]
    if task["completed"]:  # если задача выполнена
        if name not in users_tasks:  # если id пользователя нет в словаре
            users_tasks[name] = {"completed": 1, "not_completed": 0}  # создать новый ключ (id) и в значение поставитть 1
        else:  # иначе
            users_tasks[name]["completed"] += 1  # добавить к значению ключа (id) единичку
    if not task["completed"]:  # если задача выполнена
        if name not in users_tasks:  # если id пользователя нет в словаре
            users_tasks[name] = {"completed": 0, "not_completed": 1}  # создать новый ключ (id) и в значение поставитть 1
        else:  # иначе
            users_tasks[name]["not_completed"] += 1


for user in users_tasks.keys():
    print(f"User: {user};")
    print(f"Completed: {users_tasks[user]['completed']} tasks;")
    print(f"Didn't completed: {users_tasks[user]['not_completed']} tasks;")
    print()
