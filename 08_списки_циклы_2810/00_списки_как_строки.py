phrase = input('Впиши что-то: ')

"""
Чтобы превратить строчку в список,
используется метод .split(разделитель)
"""
word_list = phrase.split()  # превращаю строку в список
print(word_list)
word_list[0] = 'Пока!'  # меняю значение первого элемента списка на другое
print(word_list)
"""
Чтобы превратить список в строку, 
используется метод .join(список)
Перед методом должна находиться строка,
в которой будет символ, который будет 
подставляться между элементами списка.
"""
print(''.join(word_list))  # здесь список превратится в строчку без пробелов
c = ' '.join(word_list)  # это разделитель элементов бывшего списка
print(c)  # здесь список превратится в строчку, где между словами будут стоять пробелы
