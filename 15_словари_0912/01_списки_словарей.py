from colorama import Fore, Back  # импортируем функции окрашивания текста

students = []
action = 1  # выбор действия в меню
while action != 7:  # пока пользователь не выберет 7 (для выхода из программы)
    print(Fore.GREEN + '1 - Ввод информации о студенте\n2 - Сортировка списка студентов\n3 - Поиск студента\n4 - изменение данных студента\n5 - Удаление студента\n6 - Информация о всех студентах\n7 - выход')
    action = int(input('Выберите действие: '))
    if action == 1:  # действие - наполнить список словарями
        n = int(input('Количество студентов: '))
        # наполнение списка словарями
        for i in range(n):
            student = {
                'full_name': '',
                'address': '',
                'group': '',
                'rate': 0.0,
            }  # обнуляем значения ключей словаря student
            for key in student:  # перебираю ключи словаря
                student[key] = input(Fore.LIGHTBLUE_EX + f'value of {key}: ')  # цвет текста из инпута - голубой
            student['rate'] = eval(student['rate'])  # преобразовываю рейтинг в число
            students.append(student)  # добавляю нового студента в список
    elif action == 2:  # действие - сортировка списка словарей
        pass  # ничего не делать
    elif action == 3:  # действие - поиск по списку словарей
        # поиск по списку словарей
        rate = eval(input(Fore.RED + 'Rate of student: '))
        for i in range(len(students)):  # количество повторений = количеству студентов в списке
            if students[i]['rate'] == rate:  # если рейтинг студента совпадает с введенным
                print(students[i])  # вывести информацию об этом студенте
    elif action == 4:  # действие - изменение данных определенного студента
        n = int(input('Введите номер студента: '))
        n -= 1
        for key in students[n]:  # перебираю ключи определенного студента
            new_val = input(f'Новое значение ключа {key}: ')
            students[n][key] = new_val or students[n][key]  # записать старое значение, если ничего не передали
    elif action == 5:  # действие - удаление определенного студента
        n = int(input('Введите номер студента: '))
        n -= 1  # так как индексы начинаются с 0, студент №3 будет иметь индекс 2
        if n > len(students) or n < 0:
            print('Недопустимый номер!')
        else:
            students.pow(n)  # удалить элемент списка с индексом n
    elif action == 6:  # действие - вывести информацию о всех студентах
        print('Информация обо всех студентах: ')
        for i in range(len(students)):
            print(f'ФИО: {students[i]["full_name"]}')
            print(f'Адрес: {students[i]["address"]}')
            print(f'Группа: {students[i]["group"]}')
            print(f'Рейтинг: {students[i]["rate"]}')
            print()

    else:  # если ввели число, не совпадающее с пунктами меню
        print(Fore.RED + 'Такого пункта в меню нет!')


