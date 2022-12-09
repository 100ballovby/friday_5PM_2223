import requests as r
import json

username = input('User: ')

url = f'https://api.github.com/users/{username}/repos'
response = r.get(url)  # передаю параметры с запросом
resp_json = response.json()

# запишем ответ сервера в файлик
with open(f'{username}.json', 'w') as file:
    file.write(json.dumps(resp_json))
    # метод dumps преобразует строчку json в строку, которую можно записать в файл

with open(f'{username}.json', 'r') as f:
    # выгружаю из json-файла в словарь Python
    repos = json.loads(f.read())

for repo in repos:
    print(f'{repo["name"]}, {repo["svn_url"]}, {repo["language"]}, {repo["forks"]}')


