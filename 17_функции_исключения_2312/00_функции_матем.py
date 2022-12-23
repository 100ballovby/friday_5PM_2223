"""Аннотирование (декларация) типов
вы можете указать тип данных параметров
и тип данных возвращаемого значения функцией
при ее объявлении. Эта особенность позволяет
"подсказать" нужный тип данных при вызове функции
"""


def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    try:  # попытайся
        return a / b  # вернуть результат деления a на b
    except ZeroDivisionError:  # если возникнет исключение деления на ноль
        return "Делить на ноль нельзя"  # вернуть сообщение
    except TypeError:  # если возникает исключение неправильного типа данных (отдаются строки вместо чисел)
        return "Делить можно только числа"  # вернуть сообщение


def power(n: int, exp: int) -> int:
    res = 1
    # то, что работает в блоке try, остается в блоке try.
    # выход в общий поток программы невозможен
    try:
        for i in range(exp):
            res *= n
        return res
    except ValueError:
        return res


print('2 ^ 3 =', power(2, 3))
print(multiply(5.6, 6.4))
print(divide(4, 2))
print(divide(10, 0))
print(divide(5, '5'))

