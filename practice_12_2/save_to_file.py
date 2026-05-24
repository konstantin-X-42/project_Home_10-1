import json
import logging
from typing import Any

logger = logging.getLogger("save_to_file")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/save_to_file.log", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def save_to_file(data: list[dict[str, Any]], file_path: str) -> None:
    """Сохранение данных по указанному пути"""
    try:
        logger.info(f"Записываем данные в файл {file_path}")
        with open(file_path, "w") as data_file:
            json.dump(data, data_file)
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
