# from http.client import responses

import requests

API_KEY = "c330712acd8d1d661b710618563ef5c8"
# данные погоды по Москве
response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q=Moscow&appid={API_KEY}")

print(response.json())
# >>> {'cod': '200', 'message': 0, 'cnt': 40, 'list': [{'dt': 1778792400, 'main': {'temp': 290.14, ...
# координаты Москвы
lat = response.json()["city"]["coord"]["lat"]
lon = response.json()["city"]["coord"]["lon"]

print(f"lat = {lat}\nlon = {lon}")

# данные по координатам погоды по Москве
response__ = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
print(response__.json())
