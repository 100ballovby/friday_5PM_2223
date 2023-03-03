import requests as r
import os


def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'appid': '',
    }
    res = r.get(url, params=params)
    return res.json()


print(get_weather())
