import os

import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
BASE_URL = "https://apilayer.com"


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции из USD или EUR в RUB."""
    amount = float(transaction.get("amount", 0.0))
    currency = transaction.get("currency")

    # Если валюта уже рубли, конвертация не требуется
    if currency == "RUB":
        return amount

    # Если валюта USD или EUR, запрашиваем актуальный курс
    if currency in ["USD", "EUR"]:
        headers = {"apikey": API_KEY}
        params = {"symbols": "RUB", "base": currency}

        try:
            response = requests.get(BASE_URL, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            # Получаем курс рубля к базовой валюте
            rate = data["rates"]["RUB"]
            return float(amount * rate)

        except (requests.RequestException, KeyError, ValueError) as e:
            print(f"Ошибка при запросе курса валют: {e}")
            raise RuntimeError("Не удалось выполнить конвертацию валюты")

    # Если валюта не поддерживается
    raise ValueError(f"Неподдерживаемая валюта: {currency}")
            print(f"Ошибка при обращении к API валют: {e}")
            return 0.0

    # Если пришла какая-то другая неизвестная валюта
    return 0.0
