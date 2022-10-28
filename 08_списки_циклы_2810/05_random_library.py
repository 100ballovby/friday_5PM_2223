import random as r  # подключаю библиотеку к своему файлу/проекту

r_num = r.randint(1, 20)  # random integer
# randint(1, 10) - случайное число от 1 до 10
print(r_num)
r_double = r.uniform(0.01, 0.02)  # случайная дробь
# uniform(0.1, 0.5) - случайная дробь от 0.1 до 0.5
print(r_double)
r_elem = r.choice(['ля', 'привет', 'андрей'])  # случайный элемент из последовательности
# choice(list/str/dict/tuple) - достает случайный элемент из переданной последовательности элементов
print(r_elem)