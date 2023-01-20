def read_file(path):
    content = ''
    with open(path, 'r') as file:
        lines = file.readlines()
        # функция превращает весь файл в список строк
        for line in lines:  # перебираю строки из файла
            content += line.strip()  # .strip() убирает лишние пробелы и символы новой строки по краям
            # добавляю каждую к переменной с пустой строкой
        print(content)


def file_to_list(path):  # функция будет превращать файл в список строк
    with open(path) as file:
        content = []
        lines = file.readlines()
        for line in lines:
            content.append(line)
    return content


def file_to_dictionary(path):  # функция будет превращать файл в список строк
    with open(path) as file:
        content = {}
        lines = file.readlines()
        for line_n in range(len(lines)):
            content[line_n] = lines[line_n]
    return content


read_file('pi_digits.txt')
alice = file_to_list('alice.txt')
print(alice)
alice_dictionary = file_to_dictionary('alice.txt')
print(alice_dictionary)

