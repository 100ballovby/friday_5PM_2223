d2 = [
    {
        "name": "Иванов Иван",
        "birthday": "01/12/2000",
        "height": 170,
        "weight": 70.5,
        "car": True,
        "languages": [
            "C++",
            "Python"
        ]
    },
    {
        "name": "Сергеев Сергей",
        "birthday": "01/06/2001",
        "height": 180,
        "weight": 110.4,
        "car": False,
        "languages": [
            "Pascal",
            "Delphi"
        ]
    },
    {
        "name": "Николаева Мария",
        "birthday": "14/07/1998",
        "height": 180,
        "weight": 66.9,
        "car": True,
        "languages": [
            "C#",
            "C++",
            "C"
        ]
    }
]

for i in range(len(d2)):  # повторить <длина_d2> раз (0, 1, 2)
    print(f'Человек {i + 1}:')
    for key in d2[i]:  # перебираю ключи во вложенных словарях
        print(f'\t{key}: {d2[i][key]};')
        # d2[i][key] - обратиться к списку d2, найти словарь по индексу i и вывести значения по ключам словаря
    print()

