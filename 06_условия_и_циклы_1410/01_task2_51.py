"""Написать программу, которая
получает число n и находит его
абсолютную разницу с числом 51.
Если число n больше 51, вернуть
утроенную разницу"""
n = int(input('Введите n: '))
x = 51
if n > x:
    print((n - x) * 3)
else:
    print(x - n)


