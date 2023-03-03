import requests as r


def get_weather():
    url = "https://api.openweathermap.org/v2/weather"
    params = {}
    res = r.get(url, params=params)
    return res.json()

