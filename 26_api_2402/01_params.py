import requests as r


cur_list = {
    1: 'USD',
    2: 'GBP',
    3: 'JPY',
    4: 'BYN',
    5: 'EUR',
    6: 'BTC',
}

def menu():
    print('Валюты:\n1 - Доллар\n2 - Фунт\n3 - Йена\n4 - Бел.Руб.\n5 - Евро\n6 - Биткоин')
    choice = int(input('Ваш выбор: '))
    if choice in cur_list.keys():  # если выбор пользователя есть среди ключей словаря
        return cur_list[choice]  # возвращаем код валюты
    else:
        return 1  # вернуть единичку как сообщение об ошибке

def get_rates(currency):
    url = 'https://api.coinbase.com/v2/exchange-rates'
    query = {'currency': currency}
    response = r.get(url, params=query).json()
    return response['data']['rates']  # получаем словарь со списком курсов валют

def get_currency():
    choice = 0
    while (choice == 0 or choice == 1):  # даем пользователю шанс ввести правильное значение
        choice = menu()
        if choice == 1:
            print('\n\nНеправильный код валюты!\n')
        else:
            return choice

amount = 0
from_cur = ''
to_cur = ''
work = True

print('\t\t\t======Конвертер валют======')
while work:  # пока в переменной work = True
    print('Из какой валюты переводим?')
    from_cur = get_currency()
    amount = eval(input('Сколько денег хотите перевести? '))
    print('В какую валюту переводим?')
    to_cur = get_currency()
    rates = get_rates(from_cur)

    res = amount * float(rates[to_cur])  # отдельно сохраняю результат конвертации
    print(f'{amount} {from_cur} будет {round(res, 2)} {to_cur}')  # округляю результат конвертации до 2 знаков после запятой

    cont = int(input('1 - еще раз, 2 - выйти: '))
    if cont == 2:
        print('До свидания!')
        work = False  # остановить работу программы



