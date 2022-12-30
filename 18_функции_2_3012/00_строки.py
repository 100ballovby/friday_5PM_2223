phrase = input('Напишите что-то: ')
symbol = input('Введите символ: ')


def search_symbol(string, char):
    for i in range(len(string)):  # перебираются числа от 0 до длины строки
        if string[i] == char:
            return i


def find_numbers(string):
    numbers = []
    index = 0
    while index < len(string):
        number = ''  # здесь я буду хранить найденные числа в строке
        while string[index].isdigit():
            number += string[index]
            index += 1
        index += 1
        if number:  # если переменная number не пустая
            numbers.append(number)
        if index >= len(string):
            return numbers


def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[len(word) - 1 - i]:  # если это случилось
            return False  # функция закончится здесь
    # а если условие прошло проверку
    return True  # функция закончится здесь


def is_palindrome_v2(word):
    # вернуть логическое заключение проверки, что
    # срез слова сначала и до конца совпадает со срезом
    # слова с конца и до начала (-1 - это ход в обратную сторону)
    return word[::] == word[::-1]


words = ['казак', 'алла', 'level', 'ololo', 'попугай', 'жираф']
for i in range(len(words)):
    print(f'{words[i]} is palindrome: {is_palindrome_v2(words[i])}')




