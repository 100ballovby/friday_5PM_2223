def append_file(path, content):
    with open(path, 'a') as file:  # открыть файл в режиме append и присвоить его переменной
        file.write(content + '\n')  # записываю текст из переменной в файл
# write() может записывать ТОЛЬКО строки
append_file('primer2.txt', 'Мама мыла раму')
append_file('primer2.txt', '64389')
a = [4, 3, 2, 12, 67, 8, 19]
append_file('primer2.txt', str(a))
