"""
Датасет
titanic.csv
содержит информацию о пассажирах корабля «Титаник», включая их возраст, пол, класс билета и информацию о том,
выжили они или нет при крушении корабля. Датасет содержит 12 столбцов:

PassengerId — уникальный идентификатор пассажира.
Survived — указывает, выжил пассажир или нет (0 — не выжил, 1 — выжил).
Pclass — класс билета (1 — первый класс, 2 — второй класс, 3 — третий класс).
 Name — имя пассажира.
Sex — пол пассажира.
Age — возраст пассажира.
SibSp — количество братьев, сестер, супругов на борту.
Parch — количество родителей или детей на борту.
Ticket — номер билета.
Fare — цена билета.
Cabin — номер каюты.
Embarked — порт посадки (C — Шербур, Q — Квинстаун, S — Саутгемптон).

Задача 1
Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv
Функция должна вычислить средний возраст мужчин и женщин отдельно
и вернуть результат в виде словаря в формате JSON.
"""

import json
import os

import pandas as pd


def avg_age_by_gender(df):  # type: ignore
    avg_age_male = round(df[df["Sex"] == "male"]["Age"].mean(), 1)
    avg_age_female = round(df[df["Sex"] == "female"]["Age"].mean(), 1)
    result_dict = {"Мужчины": avg_age_male, "Женщины": avg_age_female}
    return json.dumps(result_dict, ensure_ascii=False)


# --- БЛОК ДЛЯ ПРОВЕРКИ ---
if __name__ == "__main__":

    # ВАРИАНТ 1-й ЧЕРЕЗ URL
    # # Загружаем официальный датасет Титаника напрямую из репозитория GitHub
    # url = "https://githubusercontent.com"
    # titanic_df = pd.read_csv(url)

    # ВАРИАНТ 2-й ЧЕРЕЗ директорию на компьютере
    # получаем путь к папке, где лежит этот скрипт (data_13_1)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    titanic_df = pd.read_csv(os.path.join(current_dir, "data_13_1", "titanic.csv"))

    # Вызываем вашу функцию
    json_result = avg_age_by_gender(titanic_df)  # type: ignore

    # Печатаем результат в консоль
    print("Итоговый JSON-ответ:")
    print(json_result)
