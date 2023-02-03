import json

def connect(link):
    import requests as req
    resp = req.get(link)
    return resp.json()  # возвращает ответ от сервера


url = "https://jsonplaceholder.typicode.com/todos"
con = connect(url)

url_2 = "https://jsonplaceholder.typicode.com/users"
con_2 = connect(url_2)

with open("todos.json", "w") as file:
    file.write(json.dumps(con, indent=4))

compl = 0
not_compl = 0
for task in con:
    print(f'Task {task["id"]} is completed {task["completed"]}')
    if task["completed"]:  # task["completed"] == True (если в ключе completed True)
        compl += 1
    elif not task["completed"]:  # task["completed"] == False
        not_compl += 1

print(f"{compl} tasks completed!")
print(f"{not_compl} tasks not completed!")

# TODO: создать словарь, где ключом будет id пользователя,
#  а значением количество задач, которые он выполнил
users_tasks = {}
for task in con:  # перебираю все задачи
    if task["completed"]:  # если задача выполнена, проверить наличие пользователя в словаре
        if task["userId"] not in users_tasks:  # если ключа с id НЕТ в словаре
            users_tasks[task["userId"]] = 1  # добавляю id в словарь и количество задач ставлю как 1
        else:  # если ключ с id ЕСТЬ в словаре
            users_tasks[task["userId"]] += 1  # увеличиваю количество выполненных задач у этого пользователя
print(users_tasks)

# TODO: создать словарь, где ключом будет id пользователя,
#  а значением его имя
users = {}
for user in con_2:  # перебираю каждого пользователя из списка
    users[user["id"]] = user["name"]  # создать ключ с id пользователя, а значением поставить name
print(users)

"https://t.me/python_fri_gr"
