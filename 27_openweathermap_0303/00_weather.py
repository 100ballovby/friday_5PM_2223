import requests as r
import os


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': os.environ.get('API_KEY'),  # получаем переменную среды
        'units': 'metric',
        'lang': 'ru',
        'q': city,
    }
    res = r.get(url, params=params)
    return res.json()


def show_weather(json_response):
    print(f'Город: {json_response["name"]}')
    print(f'Температура: {json_response["main"]["temp"]}')
    print(f'Ощущается как: {json_response["main"]["feels_like"]}')
    print(f'На улице {json_response["weather"][0]["description"]}')
    print(f'Максимальная температура за день: {json_response["main"]["temp_max"]}')
    print(f'Минимальная температура за день: {json_response["main"]["temp_min"]}')
    print('\n\n')

cities = ['москва', 'Санкт-Петербург', 'Minsk', 'Paris', 'Warsaw', 'New York', 'Vilnius']

for city in cities:
    ans = get_weather(city)
    show_weather(ans)
