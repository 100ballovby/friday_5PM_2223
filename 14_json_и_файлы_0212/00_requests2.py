import requests as r
import json  # методы работы с форматом JSON

url = 'https://api.github.com/search/repositories'
params = {'q': ''}  # храню запрос для поиска
query = input('Запрос для поиска: ')
params['q'] = query
response = r.get(url, params=params)  # передаю параметры с запросом
resp_json = response.json()

# запишем ответ сервера в файлик
with open('github.json', 'w') as file:
    file.write(json.dumps(resp_json))
    # метод dumps преобразует строчку json в строку, которую можно записать в файл

