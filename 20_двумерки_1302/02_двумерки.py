import random as r

matrix = [[1, 2, 4], [8, 0, 3], [9, 6, 3]]


def print_matrix(arr, lines, cols):
    for i in range(lines):  # здесь я перебираю строки матрицы
        for j in range(cols):  # Здесь я перебираю столбцы матрицы
            print(arr[i][j], end=" ")  # Вывожу каждый элемент строки
        print()   # Enter (новая строка)


def fill_matrix(lines, cols, start=0, stop=10):
    matrix = []  # создаем пустой список, который будем наполнять
    for i in range(lines):  # повторить lines раз
        line = []  # создать строку матрицы
        for j in range(cols):  # повторить cols раз
            n = r.randint(start, stop)  # сгенерировать случайное число
            line.append(n)  # Добавляю в строку матрицы случайное числоо
        matrix.append(line)  # Добавляю строку матрицы В МАТРИЦУ
    return matrix

mtrx = fill_matrix(4, 6, 1, 20)  # создать матрицу размером 5х5 и заполнить числами от 1 до 20
print_matrix(mtrx, 4, 6)
