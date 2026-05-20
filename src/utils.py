import json
from pathlib import Path
from typing import Any

# Абсолютный путь к папке src, где лежит utils.py
CURRENT_DIR = Path(__file__).resolve().parent


def get_transactions(file: str | Path) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей с транзакциями,
    файл не найден или пуст или содержит не список, возвращает пустой список.
    """
    path = Path(file)
    if not path.is_file():
        return []  # если файла по указанному пути не существует - ошибка
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []  # если тип данных не list - ошибка
    except json.JSONDecodeError, FileNotFoundError:
        return []  # содержимое файла повреждено или файл отсутствует - ошибка


# from src.utils import get_financial_transactions

# Относительный путь от корня проекта
# path_to_file = "../data/operations.json"

# Абсолютный путь к файлу operations.json
path_to_file = CURRENT_DIR.parent / "data" / "operations.json"

# Вызываем функцию
transactions = get_transactions(path_to_file)

print(transactions)
