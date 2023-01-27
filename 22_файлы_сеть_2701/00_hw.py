def write_file(filename, count):
    with open(filename, 'w') as file:
        for i in range(count):
            string = input("In python you can: ")
            file.write("In Python you can " + string)


def read_file(filename):
    res = []
    with open(filename, "r") as file:
        lines = file.readlines()  # беру все строки из файла и закидываю их в список
        for line in lines:
            res.append(line)
            print(line)
    return res


write_file("LearningPython.txt", 3)
lst = read_file("LearningPython.txt")
print(lst)


