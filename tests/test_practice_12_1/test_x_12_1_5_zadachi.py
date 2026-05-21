import json

import pytest

from practice_12_1.x_12_1_5_zadachi import filter_transactions  # Замените your_module на имя вашего файла с кодом
from practice_12_1.x_12_1_5_zadachi import generate_users  # Импортируем из файла с функцией

"""
КОМАНДА тестируем только модуль x_12_1_5_zadachi
pytest tests/test_practice_12_1/test_x_12_1_5_zadachi.py

детальный вывод в консоль
pytest -vv -s tests/test_practice_12_1/test_x_12_1_5_zadachi.py
"""


# * * * * * * * * * * * * * * * * * * * * * * * ЗАДАЧА 1 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# import pytest
# from practice_12_1.x_12_1_5_zadachi import generate_users  # Импортируем из файла с функцией


@pytest.fixture
def data():
    return {
        "first_names": ["John", "Jane", "Mark", "Emily", "Michael", "Sarah"],
        "last_names": ["Doe", "Smith", "Johnson", "Brown", "Lee", "Wilson"],
        "cities": ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia"],
    }


def test_generate_users_num_users(data):
    """Проверяет, что количество сгенерированных пользователей равно запрошенному количеству пользователей."""
    num_users = 5
    users = [next(generate_users(**data)) for _ in range(num_users)]  # type: ignore
    assert len(users) == num_users


def test_generate_users_keys(data):
    """Проверяет, что у всех сгенерированных пользователей есть правильные ключи."""
    users = [next(generate_users(**data)) for _ in range(5)]  # type: ignore
    for user in users:
        assert set(user.keys()) == {"first_name", "last_name", "age", "city"}


def test_generate_users_first_names(data):
    """Проверяет, что у всех сгенерированных пользователей имя является одним из возможных имен."""
    users = [next(generate_users(**data)) for _ in range(5)]  # type: ignore
    for user in users:
        assert user["first_name"] in data["first_names"]


def test_generate_users_last_names(data):
    """Проверяет, что у всех сгенерированных пользователей фамилия является одной из возможных фамилий."""
    users = [next(generate_users(**data)) for _ in range(5)]  # type: ignore
    for user in users:
        assert user["last_name"] in data["last_names"]


def test_generate_users_age(data):
    """Проверяет, что у всех сгенерированных пользователей возраст находится в заданном диапазоне."""
    users = [next(generate_users(**data)) for _ in range(5)]  # type: ignore
    for user in users:
        assert 18 <= user["age"] <= 65


def test_generate_users_cities(data):
    """Проверяет, что у всех сгенерированных пользователей город является одним из возможных городов."""
    users = [next(generate_users(**data)) for _ in range(5)]  # type: ignore
    for user in users:
        assert user["city"] in data["cities"]


# * * * * * * * * * * * * * * * * * * * * * * * ЗАДАЧА 2 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# import json
#
# import pytest
#
# from practice_12_1.x_12_1_5_zadachi import filter_transactions  # Замените your_module на имя вашего файла с кодом


@pytest.fixture
def sample_transactions():
    """Фикстура с базовым набором транзакций."""
    return [
        {"date": "2021-05-01", "amount": 1000, "currency": "USD", "description": "Salary"},
        {"date": "2021-05-02", "amount": -50, "currency": "EUR", "description": "Dinner"},
        {"date": "2021-05-03", "amount": -20, "currency": "USD", "description": "Coffee"},
        {"date": "2021-05-04", "amount": 200, "currency": "GBP", "description": "Gift"},
    ]


def test_filter_transactions_usd(tmp_path, sample_transactions):
    """Проверка корректности фильтрации по USD и структуры выходного файла."""
    # Создаем временные пути для файлов
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"

    # Записываем тестовые данные во входной файл
    input_file.write_text(json.dumps(sample_transactions))

    # Вызываем целевую функцию
    result = filter_transactions(str(input_file), str(output_file), "USD")

    # Проверяем возвращаемое значение функции
    assert len(result) == 2
    assert result[0]["amount"] == 1000
    assert result[1]["amount"] == -20

    # Читаем созданный выходной файл и проверяем его содержимое
    with open(output_file, "r", encoding="utf-8") as f:
        file_data = json.load(f)

    assert file_data == result
    assert all(tx["currency"] == "USD" for tx in file_data)


def test_filter_transactions_empty_result(tmp_path, sample_transactions):
    """Проверка фильтрации по валюте, которой нет в списке."""
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"
    input_file.write_text(json.dumps(sample_transactions))

    result = filter_transactions(str(input_file), str(output_file), "RUB")

    assert result == []

    with open(output_file, "r", encoding="utf-8") as f:
        file_data = json.load(f)
    assert file_data == []


def test_decorator_stdout(tmp_path, sample_transactions, capsys):
    """Проверка вывода статистики декоратором в консоль."""
    input_file = tmp_path / "input.json"
    output_file = tmp_path / "output.json"
    input_file.write_text(json.dumps(sample_transactions))

    # Вызываем функцию (декоратор сработает внутри)
    filter_transactions(str(input_file), str(output_file), "USD")

    # Перехватываем вывод в консоль с помощью фикстуры capsys
    captured = capsys.readouterr()

    # Проверяем наличие ключевых строк статистики в выводе
    assert "СТАТИСТИКА ФИЛЬТРАЦИИ:" in captured.out
    assert "Количество транзакций: 2" in captured.out
    assert "Суммарная стоимость: 980" in captured.out
