"""
Дан список длиной n. Нужно найти
наибольший по модулю элемент списка
"""
import random as r
import math as m

arr = []
n = int(input('Сколько чисел нужно? '))
for i in range(n):  # количество повторений равно значению n
    arr.append(r.randint(-100, 100))  # добавить в список случайное число от -100 до 100
print(arr)

maximum = arr[0]  # первый элемент списка считаю самым большим
index_max = 0  # индекс самого большого элемента 0
for i in range(1, len(arr)):  # перебираю индексы элементов со второго до конца
    if m.fabs(arr[i]) > m.fabs(maximum):  # если конкретный элемент списка (с индексом i) больше максимума
        maximum = arr[i]  # делаю этот элемент максимальным
        index_max = i  # записываю индекс этого элемента в п переменную
print('Наибольший по модулю элемент', maximum)
print('Индекс наибольшего элемента', index_max)

