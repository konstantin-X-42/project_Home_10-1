import os  # сопрягает работу кода с Windows, macOS или Linux

# импортируем чтобы Python-код мог находить, открывать, создавать файлы или переходить между папками на компьютере.
from pathlib import Path
from typing import Any  # импортируем тип Any - любой тип данных

import requests  # импортируем библиотеку нужна для отправки HTTP-запросов в интернет.
from dotenv import load_dotenv  # функция заходит в файл (.env)

"""
устанавливаем библиотеку библиотеку requests — инструмент в Python для отправки HTTP-запросов в интернет.
poetry add requests
"""

"""
устанавливаем библиотеку python-dotenv - безопасно разделяет мой программный код
и секретные данные (пароли, токены, ключи API), умеет автоматически находить текстовый файл .env

poetry add python-dotenv
"""
# ----------
"""извлекаем в переменную конфиденциальные данные"""
current_dir = Path(__file__).resolve().parent  # находим путь к папке, где
# лежит запускаемый скрипт x_12_1_10_mock_and_patch.py
base_dir = current_dir.parent  # переходим на одну папку выше в project_Home_10_1
load_dotenv(base_dir / ".env")  # указываем место .env / подгружает настройки из скрытого файла (.env) в память
API_KEY = os.getenv("API_KEY")  # извлекаем ключ из памяти и записываем в API_KEY (переменная Python)


def get_data(city: str) -> dict[str, Any]:
    """Получение данных погоды по названию города (Moscow)"""
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric")
    data: dict[str, Any] = response.json()  # # применяем линтеру data — это словарь
    return data


# print(get_data("Moscow"))


def get_coordinates(city: str) -> tuple[float, float]:
    """Получение координат по названию города"""
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}")
    latitude = response.json()["city"]["coord"]["lat"]
    longitude = response.json()["city"]["coord"]["lon"]
    return latitude, longitude


# print(get_coordinates("Moscow"))


def get_weather(latitude: float, longitude: float) -> Any:
    """Получение температуры по координатам"""
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    )
    data: dict[str, Any] = response.json()
    return data["main"]["temp"]


if (
    __name__ == "__main__"
):  # проверяет, запущен файл напрямую (как основная программа) или импортирован в другой скрипт
    latitude, longitude = get_coordinates("Moscow")
    print(get_weather(latitude, longitude))
