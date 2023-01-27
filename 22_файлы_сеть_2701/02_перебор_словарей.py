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

person = data["employees"][1]

# перебор словаря по ключам:
for key in person.keys():  # здесь должен быть словарь
    print(f"Ключ: {key}")


# перебор словаря по значения v1
for key in person.keys():  # здесь должен быть словарь
    print(f"Значение: {person[key]}")

# перебор словаря по значению v2
for value in person.values():  # здесь должен быть словарь
    print(f"Значение: {value}")

# перебор одновременно ключей и значений словаря
for key, value in person.items():
    print(f"Key: '{key}', Value: '{value}';")


primer = [[0, 1], [2, 3], [3, 4], [5, 6]]
for i1, i2 in primer:  # i1 = 0, i2 = 1; i1 = 2, i2 = 3....
    print(i1, i2)

