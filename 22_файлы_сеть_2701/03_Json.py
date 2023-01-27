import json

data = {
    'employees': [
        {
            'name': 'John Doe',
            'department': 'Marketing',
            'place': 'Remote'
        },  # индекс 0
        {
            'name': 'Jane Doe',
            'department': 'Software Engineering',
            'place': 'Remote'
        },  # индекс 1
        {
            'name': 'Don Joe',
            'department': 'Software Engineering',
            'place': 'Office'
        }  # индекс 2
    ]
}


"""
dump() - превращает словарь/список в поток данных JSON для записи в файл 
dumps() - превращает словарь/список в СТРОКУ в формате JSON 
"""


def dict_to_json(obj, filename):
    json_str = json.dumps(obj, indent=4)  # indent=4 позволяет красиво записать json в файлик
    with open(filename, "w") as json_file:
        # json.dump(obj, filename, indent=4) <- записывайте в файл без функции write
        json_file.write(json_str)


def json_to_dict(filename):
    with open(filename, "r") as json_file:
        dictionary = json.load(json_file)  # превращает строку JSON в словарь Python
    return dictionary


dict_to_json(data, "employees.json")  # перевод словаря в JSON
res = json_to_dict("employees.json")  # перевод JSON'а в словарь
print(type(res))


