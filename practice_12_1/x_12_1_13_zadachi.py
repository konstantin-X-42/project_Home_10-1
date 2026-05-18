import json
from datetime import datetime, timedelta

"""
каманда запускаем текущий модуль в тест, результат в консоль
pytest practice_12_1/x_12_1_13_zadachi.py

подробный вывод
pytest practice_12_1/x_12_1_13_zadachi.py -vv
"""

"""
Задача 1
Напишите функцию, которая принимает список дат в формате списка строк, например
["2022.12.31", "2023.1.7"] и возвращает список дат в формате строк через одну неделю, например
["January 7, 2023", "January 14, 2023"]
"""

# from datetime import datetime, timedelta


def add_week_to_dates(dates: list[str]) -> list[str]:
    output_dates = []
    for date in dates:
        date_obj = datetime.strptime(date, "%Y.%m.%d")  # создаём объект даты в память Python
        new_date_obj = date_obj + timedelta(days=7)  # к объекту даты добавляем 7 дней
        # добавляем в конец списка, преобразованный объект в строку в формате заданного шаблона
        output_dates.append(new_date_obj.strftime("%B %#d, %Y"))
    return output_dates


print(add_week_to_dates(["2022.12.31", "2023.1.7"]))


"""
Тесты:
"""


def test_add_week_to_dates() -> None:
    """проверяем корректность выводимых данных"""
    assert add_week_to_dates(["2022.12.31", "2023.1.7"]) == ["January 7, 2023", "January 14, 2023"]

    """проверяем корректность вывода если подаём пустой список"""
    assert add_week_to_dates([]) == []


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
Задача 2
Напишите функцию, которая принимает JSON-строку с данными о различных событиях,
включающих даты начала и окончания, и возвращает список длительностей каждого события в днях.
Пример входных данных:
[
  {
    "name": "Event 1",
    "start_date": "2022-01-01",
    "end_date": "2022-01-05"
  },
  {
    "name": "Event 2",
    "start_date": "2022-02-15",
    "end_date": "2022-02-18"
  },
  {
    "name": "Event 3",
    "start_date": "2022-03-10",
    "end_date": "2022-03-20"
  }
]
Пример выходных данных:

[5, 4, 11]
"""
# import json
# from datetime import datetime


def event_durations(json_str: str) -> list[int]:
    events = json.loads(json_str)
    durations = []
    for event in events:
        start_date = datetime.strptime(event["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(event["end_date"], "%Y-%m-%d")
        duration = (end_date - start_date).days
        durations.append(duration)
    return durations


"""Тесты:"""


def test_event_durations() -> None:
    json_str = (
        '[{"name": "Event 1", "start_date": "2022-01-01", "end_date": "2022-01-05"},'
        ' {"name": "Event 2", "start_date": "2022-02-15", "end_date": "2022-02-18"},'
        ' {"name": "Event 3", "start_date": "2022-03-10", "end_date": "2022-03-20"}]'
    )
    assert event_durations(json_str) == [4, 3, 10]
