phrase = input('Введи фразу: ')
words = phrase.split()
counter = 0  # количество палиндромов
for word in words:  # перебираю каждое слово в списке
    if word == word[::-1] and len(word) > 2:
        # если слово слева-направо выглядит так же, как справа-налево и оно длиннее 2 букв
        counter = counter + 1

print('Количество палиндромов:', counter)
