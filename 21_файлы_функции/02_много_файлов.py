import os


def create_file(path):
    with open(path, 'w') as file:
        file.write('import os\nprint(os.listdir())')
        for i in range(1000000):
            file.write('\n')


os.mkdir('test_folder1')  # создать папку (там, где запускается файл) с названием test_folder1
for i in range(1000):  # тысячу раз
    create_file(f'test_folder1/file_{i}.py')  # вызвать функцию, создающую файл