import json
from pathlib import Path
from typing import Any

# Импортируем функцию настройки логгера из файла log_config текущей директории
from src.log_config import module_logger

# Инициализируем логгер (задаем имя файлу, имя логгеру, дозапись-False,
# перезапись-True; лог в файл и консоль-True, в файл-False)
log = module_logger(file_name="utils.log", logger_name="logs", overwrite=False, log_console=True)
# -------------------------------------------------------

# Абсолютный путь к папке src, где лежит utils.py для файла JSON
CURRENT_DIR = Path(__file__).resolve().parent


def get_transactions(file: str | Path) -> list[dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей с транзакциями,
    файл не найден или пуст или содержит не список, возвращает пустой список.
    """
    log.info(f"Функция инициализирована с аргументом: {file}")
    path = Path(file)
    if not path.is_file():
        log.error("JSON-файл не существует, возвращаем []")
        return []
    try:
        with open(path, "r", encoding="utf-8") as json_file:  # открываем JSON-файл на чтение
            data = json.load(json_file)  # читаем JSON-файл и преобразуем в тип данных Python
            if isinstance(data, list):  # обрабатываем только тип данных List[]
                log.info("Успешно")
                return data
            log.error(f"Функция обрабатывает: <class 'list'>, тип данных JSON-файла: {type(data)}, возвращаем []")
            return []  # иной тип данных, не list - ошибка
    except json.JSONDecodeError, FileNotFoundError:
        log.error("Содержимое JSON-файла повреждено или JSON-файл отсутствует, возвращаем []")
        return []


# -----------вызываем функцию------------
# Относительный путь от корня проекта
# path_to_file = "../data/operations.json"

# Абсолютный путь к файлу operations.json
# path_to_file = CURRENT_DIR.parent / "data" / "operations.json"

# print(get_transactions(path_to_file))
