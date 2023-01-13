str_list = ["abc", "xyz", "df", "abba", "8768", "color", "loft", "d", "ghjk"]


def search_hw(array):
    c = 0  # Здесь я буду считать КОЛИЧЕСТВО строк
    for i in range(len(array)):
        if len(array[i]) > 2 and array[i][0] == array[i][-1]:
            c += 1
    return c


print(search_hw(str_list))
