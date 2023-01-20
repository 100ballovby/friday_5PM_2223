with open('primer.txt', 'a') as file:  # открыть файл в режиме append и присвоить его переменной
    print('Я открыл файл!')
    phrase = input('Введи текст:')
    file.write(phrase + '\n')  # записываю текст из переменной в файл
