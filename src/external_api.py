import os
from pathlib import Path
from typing import Any
import requests
from dotenv import load_dotenv

# Находим путь к файлу .env и загружаем переменные окружения
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

API_KEY = os.getenv("CURRENCY_API_KEY")
# Базовый URL для Exchange Rates Data API
BASE_URL = "https://apilayer.com"


def convert_rub(transaction: dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли.

    Если валюта USD или EUR, запрашивает актуальный курс через внешнее API.
    Если валюта уже RUB, возвращает исходную сумму.
    """
    # Достаем данные о сумме и валюте из словаря транзакции
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount")
    currency = operation_amount.get("currency", {}).get("code")

    # Если данных нет, возвращаем 0.0
    if not amount_str or not currency:
        return 0.0

    # Явно приводим сумму к типу float
    amount = float(amount_str)

    # Если транзакция уже в рублях, конвертация не требуется
    if currency == "RUB":
        return amount

    # Если транзакция в USD или EUR, делаем запрос к API
    if currency in ["USD", "EUR"]:
        api_key = os.getenv("CURRENCY_API_KEY")
        if not api_key:
            raise ValueError("API-ключ 'CURRENCY_API_KEY' не найден в переменных окружения.")

        # Настраиваем заголовки и параметры запроса
        headers = {"apikey": api_key}
        params = {"to": "RUB", "from": currency, "amount": amount}

        try:
            # Выполняем GET-запрос к API
            response = requests.get(BASE_URL, headers=headers, params=params)
            response.raise_for_status()  # Проверяем статус ответа (например, на ошибку 401)

            data = response.json()
            # API возвращает результат в ключе 'result'
            result = data.get("result")

            if result is not None:
                return float(result)
            else:
                raise KeyError("Ключ 'result' отсутствует в ответе API.")

        except requests.RequestException as e:
            print(f"Ошибка при обращении к API валют: {e}")
            return 0.0

    # Если пришла какая-то другая неизвестная валюта
    return 0.0