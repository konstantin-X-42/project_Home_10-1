from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str) -> Iterator[dict[str, Any]]:
    """
    Генератор, фильтрует транзакции по заданной валюте
    """
    for transaction in transactions:
        # Безопасно достаем код валюты через .get(), чтобы избежать ошибок, если ключа нет
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


# --- Блок данных для проверки (те самые "ваши данные") ---
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614695963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

# --- Вызов функции и проверка результата ---
if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, "USD")

    # Выводим результаты по очереди
    for _ in range(2):
        try:
            print(next(usd_transactions))
        except StopIteration:
            print("Транзакции в этой валюте закончились.")

# def filter_by_currency(data: list[dict[str, Any]]) -> Iterator[dict[str, Any]]:
#     pass
#
#
# def transaction_descriptions(data: list[dict[str, Any]]) -> Iterator[str]:
#     pass


# card_number_generator
