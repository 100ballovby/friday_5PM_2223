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

# просмотрим список employees
print(data["employees"])
# хочу получить второй словарь из списка employees
print(data["employees"][1])
# хочу получить имя человека, который записан в третьем словаре списка employees
print(data["employees"][2]["name"])
