import json

with open('github.json', 'r') as f:
    # выгружаю из json-файла в словарь Python
    repos = json.loads(f.read())  # эта переменная является словарем

# выведем названия и ссылки на репозитории
for repo in repos['items']:
    print(f'Name "{repo["name"]}", link {repo["svn_url"]}, language: {repo["language"]}')

