person = {
    "name": "John Doe",  # пара "ключ: значение"
    "salary": 20000,
    "age": 38,
    "city": "Warsaw",
}

print(type(person))  # <class 'dict'>


# обращение к конкретному значению
print(person["city"])


# замена значения в словаре
person["salary"] = 17000
print(person)  # вывод всего словаря


# чтобы удалить значение БЕЗ ключа
person["age"] = None  # по факту заменили 38 на None

# чтобы удалить пару ключ-значение
del person["salary"]
print(person)

# нельзя обращаться к ключам, которых нет
# print(person["married"]) <- KeyError
# чтобы добавить новую пару в словарь, нужно
# написать ключ, которого нет и присвоить ему значение
person["married"] = True  # добавляется новая пара в конец словаря
print(person)








