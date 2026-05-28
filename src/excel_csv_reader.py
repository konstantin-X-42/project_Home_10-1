import csv
import os

def transactions_csv(file_path: str) -> list[dict]:
    """Считывает финансовые операции из CSV-файла.

    :param file_path: Путь к файлу CSV с данными транзакций.
    :return: Список словарей, где каждый словарь — это одна операция.
    """
    transactions = []

    # utf-8-sig автоматически удаляет невидимый маркер BOM, который часто создает Excel
    with open(file_path, mode="r", encoding="utf-8-sig") as file:
        # DictReader автоматически использует первую строку файла как ключи словаря
        reader = csv.DictReader(file)

        for row in reader:
            # Превращаем row (объект DictRow) в обычный словарь Python
            transactions.append(dict(row))

    return transactions

#  --  --  --  --  --  --  --  --  --  --  --  --  --

# --- БЛОК ИНИЦИАЛИЗАЦИИ ФУНКЦИИ ---
if __name__ == "__main__":

    # 1. Автоматически определяем путь к папке со скриптом
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 2. Собираем абсолютный путь к файлу внутри папки: data
    # Модуль excel_csv_reader.py лежит в src/, папка data в корне проекта, поднимаемся на один уровень вверх:
    path = os.path.abspath(os.path.join(current_dir, "..", "data", "transactions.csv"))

    print(transactions_csv(path))

# --------------------------------------------------------------------
