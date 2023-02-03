import json
def create_dict(count):
    """
    Функция получает количество человек,
    запрашивает данные о каждом и записывает
    эту информацию в словарь. Словари с инфой
    о работниках записываются в список, а список
    возвращается функцией как результат работы
    :param count: количество работников
    :return: список с информацией о работниках
    """
    persons = []  # здесь будем хранить данные о работниках
    for worker in range(count):  # для каждого работника
        person = {
            "name": "",
            "age": "",
            "department": "",
            "city": "",
        }  # создать пустой словарь
        for key in person.keys():  # перебираю ключи
            d = input(f'{key}: ')  # запрашиваю информацию для ключа
            person[key] = d  # записываю ее под этим ключом в словарь
        persons.append(person)  # добаляю нового человека в список
    return persons


empl = create_dict(3)
with open("peoples.json", "w") as json_file:
    json_file.write(json.dumps(empl, indent=4))






