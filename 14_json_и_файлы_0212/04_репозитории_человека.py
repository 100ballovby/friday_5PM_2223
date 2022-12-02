import requests as r
import json  # методы работы с форматом JSON

url = 'https://api.github.com/users/GreatRaksin/repos'
response = r.get(url)  # передаю параметры с запросом
resp_json = response.json()

# запишем ответ сервера в файлик
with open('GreatRaksin_github.json', 'w') as file:
    file.write(json.dumps(resp_json))
    # метод dumps преобразует строчку json в строку, которую можно записать в файл

with open('GreatRaksin_github.json', 'r') as f:
    # выгружаю из json-файла в словарь Python
    repos = json.loads(f.read())  # эта переменная является словарем


for repo in repos:
    print(repo)


