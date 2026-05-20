import json
import os
from pathlib import Path
from typing import Any

# import requests
from dotenv import load_dotenv  # , load_workbook

# Абсолютный путь к папке src, где лежит utils.py для файла JSON
CURRENT_DIR = Path(__file__).resolve().parent


def get_transactions(file: str | Path) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей с транзакциями,
    файл не найден или пуст или содержит не список, возвращает пустой список.
    """
    path = Path(file)
    if not path.is_file():
        return []  # если файла по указанному пути не существует - ошибка
    try:
        with open(path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                return data
            return []  # если тип данных не list - ошибка
    except json.JSONDecodeError, FileNotFoundError:
        return []  # содержимое файла повреждено или файл отсутствует - ошибка


# -----------вызываем функцию------------------------------
# Относительный путь от корня проекта
# path_to_file = "../data/operations.json"

# Абсолютный путь к файлу operations.json
path_to_file = CURRENT_DIR.parent / "data" / "operations.json"

print(get_transactions(path_to_file))


# --------------------------------------------------------------------


# Загружаем переменные окружения из .env в корне проекта
env_path = Path(__file__).resolve().parent.parent / ".env"  # библиотека pathlib вычисляется точный путь до файла .env
load_dotenv(dotenv_path=env_path)  # открывает и читает файл .env и делает доступным для Python

# print("Проверка ключа:", os.getenv("CURRENCY_API_KEY"))

API_KEY = os.getenv("CURRENCY_API_KEY")
BASE_URL = "https://apilayer.com"


def conversion_rub(amount: float, from_currency: str) -> float:
    """Конвертирует сумму из указанной валюты (USD/EUR) в RUB через API.

    Если API недоступно или ключ отсутствует, возвращает 0.0.
    """
    if not API_KEY:
        print("Ошибка: API-ключ не найден в переменных окружения.")
        return 0.0

    headers = {"apikey": API_KEY}
    params = {"to": "RUB", "from": from_currency, "amount": amount}


print(conversion_rub(102.53, "USD"))
print(conversion_rub(102.53, "RUB"))
