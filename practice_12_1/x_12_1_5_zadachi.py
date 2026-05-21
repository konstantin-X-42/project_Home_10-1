import functools
import json
import random

"""
Задача 1
Напишите функцию:  generate_users(first_names, last_names, cities), которая будет генерировать случайных пользователей.
Функция должна возвращать генератор, который будет выдавать каждого пользователя по одному в виде словаря.
Каждый пользователь должен иметь следующие данные:  first_name — имя из списка first_names;
last_name — фамилия из списка last_names;   age — возраст от 18 до 65 лет;  city — город из списка cities.
Сгенерируйте группу пользователей и выведите ее списком в консоль в формате JSON.
"""
# import json
# import random


def generate_users(first_names, last_names, cities):  # type: ignore
    """Генератор случайных пользователей."""
    while True:
        yield {
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "age": random.randint(18, 65),
            "city": random.choice(cities),
        }


if __name__ == "__main__":
    # Исходные данные для генерации
    names = ["Иван", "Анна", "Сергей", "Мария", "Петр"]
    surnames = ["Иванов", "Петрова", "Смирнов", "Кузнецова", "Попов"]
    towns = ["Москва", "Санкт-Петербург", "Новосибирск", "Казань"]

    # Получение генератора
    user_generator = generate_users(names, surnames, towns)  # type: ignore

    # Генерация группы из 3 пользователей с помощью list comprehension
    users_group = [next(user_generator) for _ in range(3)]

    # Конвертация списка в формат JSON и вывод в консоль
    # ensure_ascii=False сохраняет кириллицу, indent=4 красиво форматирует текст
    json_output = json.dumps(users_group, ensure_ascii=False, indent=4)
    print(json_output)
"""
>>> [
        {
            "first_name": "Мария",
            "last_name": "Кузнецова",
            "age": 51,
            "city": "Москва"
        },
        {
            "first_name": "Иван",
            "last_name": "Попов",
            "age": 54,
            "city": "Казань"
        },
        {
            "first_name": "Мария",
            "last_name": "Иванов",
            "age": 35,
            "city": "Санкт-Петербург"
        }
    ]
"""


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
Задача 2
Напишите программу, которая будет принимать на вход JSON-файл с данными о финансовых транзакциях,
фильтровать транзакции, совершенные в определенной валюте, и сохранять отфильтрованные данные в новый JSON-файл.
Также напишите декоратор, который будет выводить в консоль статистику по количеству отфильтрованных транзакций.
Статистика должна включать в себя количество отфильтрованных транзакций и их суммарную стоимость.

Пример входных данных (transactions.json):
[
    {
        "date": "2021-05-01",
        "amount": 1000,
        "currency": "USD",
        "description": "Salary"
    },
    {
        "date": "2021-05-02",
        "amount": -50,
        "currency": "EUR",
        "description": "Dinner"
    },
    {
        "date": "2021-05-03",
        "amount": -20,
        "currency": "USD",
        "description": "Coffee"
    },
    {
        "date": "2021-05-04",
        "amount": 200,
        "currency": "GBP",
        "description": "Gift"
    }
]
Пример выходных данных (transactions_filtered.json):
[
    {
        "date": "2021-05-01",
        "amount": 1000,
        "currency": "USD",
        "description": "Salary"
    },
    {
        "date": "2021-05-03",
        "amount": -20,
        "currency": "USD",
        "description": "Coffee"
    }
]
"""

# import functools
# import json


def transaction_stats(func):  # type: ignore
    """Декоратор для подсчета статистики по отфильтрованным транзакциям."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # type: ignore
        # Выполняем основную функцию фильтрации и сохранения
        filtered_data = func(*args, **kwargs)

        # Считаем количество и сумму (берем модуль abs для корректного учета оборота
        # или оставляем со знаком в зависимости от бизнес-логики. Здесь считаем сумму по факту).
        count = len(filtered_data)
        total_amount = sum(tx["amount"] for tx in filtered_data)

        # Выводим статистику в консоль
        print("-" * 40)
        print("СТАТИСТИКА ФИЛЬТРАЦИИ:")
        print(f"Количество транзакций: {count}")
        print(f"Суммарная стоимость: {total_amount}")
        print("-" * 40)

        return filtered_data

    return wrapper


@transaction_stats
def filter_transactions(input_file, output_file, target_currency):  # type: ignore
    """Фильтрует транзакции по валюте и сохраняет в новый файл."""
    # Чтение исходного JSON-файла
    with open(input_file, "r", encoding="utf-8") as file:
        transactions = json.load(file)

    # Фильтрация данных
    filtered = [tx for tx in transactions if tx.get("currency") == target_currency]

    # Запись отфильтрованных данных в новый JSON-файл
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(filtered, file, ensure_ascii=False, indent=4)

    return filtered


# --- Демонстрация работы программы ---
if __name__ == "__main__":
    # 1. Тестовый файл transactions.json
    sample_data = [
        {
            "date": "2021-05-01",
            "amount": 1000,
            "currency": "USD",
            "description": "Salary",
        },
        {
            "date": "2021-05-02",
            "amount": -50,
            "currency": "EUR",
            "description": "Dinner",
        },
        {
            "date": "2021-05-03",
            "amount": -20,
            "currency": "USD",
            "description": "Coffee",
        },
        {
            "date": "2021-05-04",
            "amount": 200,
            "currency": "GBP",
            "description": "Gift",
        },
    ]

    with open("x_12_1_5_transactions.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=4)

    # 2. Вызываем функцию фильтрации по валюте 'USD'
    filter_transactions(
        input_file="x_12_1_5_transactions.json",
        output_file="x_12_1_5_transactions_filtered.json",
        target_currency="USD",
    )
