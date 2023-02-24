import json
import requests as r


url = "https://api.coinbase.com/v2/exchange-rates"
url2 = "https://api.coinbase.com/v2/currencies"
ans = r.get(url)
ans2 = r.get(url2)


def make_file(filename, data):
    with open(filename, 'w') as file:
        file.write(json.dumps(data, indent=4))

def read_file(filename):
    with open(filename, 'r') as file:
        return json.loads(file.read())

make_file("rates.json", ans.json())
make_file("cur.json", ans2.json())
rates = read_file("rates.json")
curr = read_file("cur.json")

data = rates['data']['rates']  # мы сохраняем список словарей с курсами валют

amount = float(input('Введите количество денег: '))

for code in range(len(curr["data"])):
    c_code = curr["data"][code]["id"]  # сохраняю банковский код валюты
    print(f'${amount} is {amount * float(rates["data"]["rates"][c_code])} of {curr["data"][code]["name"]}')


