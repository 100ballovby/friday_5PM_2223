# напишем функцию, которая из 3 цифр создает трехзначное число
def spam(x: int, y: int = 0, z: int = 0) -> int:
    """
    Функция формирует трехзначное число на основе 3 цифр, переданных
    через аргументы
    :param x: разряд сотен
    :param y: разряд десятков (по умолчанию 0)
    :param z: разряд единиц (по умолчанию 0)
    :return: целое трехзначное число
    """
    return 100 * x + 10 * y + z

# если функция содержит параметры, значения которых
# заданы по умолчанию, аргументы можно не передавать
# !!! Параметры по умолчанию могут находиться только в конце
print(spam(3, 7, 2))
print(spam(1, 5))
print(spam(1))
print(round(5.789))  # 6
print(round(3.14157823762, 2))  # 3.14


def s_circle(r: int = 10) -> float:
    """
    Функция считает площадь круга по радиусу
    :param r: радиус
    :return: площадь - дробь
    """
    pi = 3.14
    return pi * r ** 2


print(s_circle(9))
print(s_circle())


