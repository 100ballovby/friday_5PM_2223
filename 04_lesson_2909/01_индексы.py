phrase = 'hello'
# обращение к индексу переменная[индекс]
print(phrase[0])  # достаю символ по индексу
print(phrase[-1])  # достаю последний символ строки
print(phrase.index('h'))  # достаю индекс по символу

phrase = 'Привет, Андрей! Зачем ты плюнул в голубей?'
symbol = input('Введите символ: ')
if symbol in phrase:  # если символ найден в строке
    print(phrase.index(symbol))  # вывести номер этого символа
else:
    print('Символа', symbol, 'в строке нет')

