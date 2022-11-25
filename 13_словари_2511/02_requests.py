import requests as req

url = 'https://jsonplaceholder.typicode.com/albums'
url_users = 'https://jsonplaceholder.typicode.com/users'

response = req.get(url)  # подключаюсь к ресурсу по URL-адресу и забираю список альбомов
response_user = req.get(url_users)  # подключаюсь к ресурсу по URL И забираю список пользователей

users = {}  # здесь буду хранить id и имена пользователей

if response.status_code == 200:  # если подключение совершено успешно
    resp_json = response.json()  # сохраняю список альбомов в формате JSON
    user_json = response_user.json()  # сохраняю список пользователей в формате JSON
else:
    print('Что-то пошло не так.')

for i in range(len(user_json)):  # перебираю список пользователей в JSON
    id = user_json[i]['id']  # ключ - это порядковый номер пользователя в базе
    name = user_json[i]['name']  # значение ключа - имя пользователя в базе
    users[id] = name  # в качестве ключа выступает id, в качестве значения - имя

print(users)

for i in range(len(resp_json)):
    if resp_json[i]['id'] <= 30:  # порядковый номер альбома меньше или равен 30
        print(f'id {resp_json[i]["id"]}: {resp_json[i]["title"]}')
        user_id = resp_json[i]["userId"]  # достаю порядковый номер автора из списка с альбомами
        print(f'Album author: {users[user_id]}')  # из списка пользователей по ID достаю имя
        # resp_json[i]["userId"] - обращается к ключу userId у каждого альбома (это число)
        # полученное число я запрашиваю в словаре users. В него мы сохранили как ключи
        # id пользователей, а как значения - их имена

