def create_array(length: int):
    arr = []
    for i in range(length):
        arr.append(0)
    return arr


def print_array(arr: list, length: int):
    try:
        for i in range(length):
            print(arr[i], end=",\t")
        print()
    except IndexError:
        print('Index Error')


def fill_array_key(arr: list, length: int):
    try:
        for i in range(length):
            arr[i] = int(input(f'Введите элемент №{i}'))
        return arr
    except IndexError:
        print('Index Error')


def fill_array_auto(arr: list, length: int, start: int, end: int):
    import random as r
    try:
        for i in range(length):
            arr[i] = r.randint(start, end)
        return arr
    except IndexError:
        print('Index Error')


def bubble_sort(arr: list, length: int):
    for i in range(length - 1):
        """range(length) тоже будет работать, но в таком 
        случае внешний цикл будет делать на одно повторение 
        больше, чем нужно по умолчанию мы считаем, что 
        последний элемент массива находится на своем 
        месте (он уже отсортирован)"""
        for j in range(length - 1 - i):
            """"Внутренний цикл просматривает 
            массив с 0 индекса до последнего - i, потому 
            что последний элемент массива уже отсортирован, 
            соответственно проверять и сортировать его еще раз 
            нет необходимости."""
            if arr[j] > arr[j + 1]:  # если текущий элемент больше следующего
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # arr[j] = arr[j + 1], arr[j + 1] = arr[j]
    return arr


def find_max(arr: list, length: int):
    i_max = 0  # индекс максимального элемента
    for i in range(length):
        if arr[i] > arr[i_max]:  # если элемент, который мы просматриваем больше максимального
            i_max = i  # присвоить индекс максимального элемента
    return i_max


def remove_duplicates(arr: list, length: int):
    unique = []
    for i in range(length):
        if arr[i] not in unique:  # если число из оригинального массива не представлено в массиве unique
            unique.append(arr[i])  # добавить его
    return unique


def count_freq(arr: list, length: int, elem: int):
    freq = 0
    for i in range(length):
        if arr[i] == elem:
            freq += 1
    return freq


# наполнение
size = 100
array = create_array(size)
#array = fill_array_key(array, size)
array = fill_array_auto(array, size, -10, 10)
print_array(array, size)

# поиск наибольшего
ind_m = find_max(array, size)  # индекс найденного наибольшего вернется в переменную ind_m
print(f'Наибольший элемент: {array[ind_m]}')

# посчитаем повторения элементов массива
el = int(input('Введи элемент: '))
found = count_freq(array, size, el)
print(f'{el} встречается в массиве {found} раз.')

# сортировка
sorted_arr = bubble_sort(array, size)
print_array(sorted_arr, size)

# убрать повторяшки
array = remove_duplicates(array, size)
# так как длина возможно изменилась, заново измеряем длину массива
size = len(array)
print_array(array, size)




