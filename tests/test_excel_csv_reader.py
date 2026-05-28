#  --  --  --  --  --  --  --  --  --  --  --  --  --
'''
Команда запуск теста ошибки в консоль
pytest -s tests/test_excel_csv_reader.py

Команда запуск теста
poetry run pytest tests/test_excel_csv_reader.py
'''
#  --  --  --  --  --  --  --  --  --  --  --  --  --
# import pytest
# from src.excel_csv_reader import transactions_csv  # импортируем функцию
#
#
# def test_transactions_csv(tmp_path):
#     # 1. Создаем временный тестовый CSV-файл
#     test_csv = tmp_path / "transactions.csv"
#     test_csv.write_text(
#         "id,state,date,amount,currency,description,from,to\n"
#         "650703,EXECUTED,2023-12-05,1500.50,RUB,Перевод,Счет,Счет\n",
#         encoding="utf-8"
#     )
#
#     # 2. Вызываем тестируемую функцию
#     result = transactions_csv(str(test_csv))
#
#     # 3. Проверяем возвращаемое значение (Assertions)
#     assert isinstance(result, list), "Функция должна возвращать список"
#     assert len(result) == 1, "В списке должна быть ровно одна запись"
#     assert isinstance(result[0], dict), "Элемент списка должен быть словарем"
#
#     # Проверяем корректность парсинга полей
#     assert result[0]["id"] == "650703"
#     assert result[0]["amount"] == "1500.50"
#     assert result[0]["description"] == "Перевод"

#  --  --  --  --  --  --  --  --  --  --  --  --  --
#  --  --  --  --  --  --  --  --  --  --  --  --  --

from unittest.mock import mock_open, patch

import pytest

from src.excel_csv_reader import transactions_csv #bvgjhnbh.n


@patch("csv.DictReader")
def test_transactions_csv_success(mock_dict_reader):
    """Тест успешного чтения данных из CSV с использованием mock."""

    # 1. Готовим фейковые данные, которые якобы вернет csv.DictReader
    mock_rows = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "amount": "1500.50",
            "currency": "RUB",
        },
        {
            "id": "123456",
            "state": "PENDING",
            "amount": "100.00",
            "currency": "USD",
        },
    ]

    # Настраиваем mock: при итерации по DictReader он должен возвращать наши словари
    mock_dict_reader.return_value = mock_rows

    # 2. Мокаем встроенную функцию open, чтобы Python не искал файл на диске
    # mock_open() создает имитацию файла
    with patch("builtins.open", mock_open(read_data="")):
        # Вызываем вашу функцию с любым вымышленным путем
        result = transactions_csv("fake_path.csv")

    # 3. Проверяем результаты (assert)
    assert len(result) == 2
    assert result[0]["id"] == "650703"
    assert result[1]["currency"] == "USD"
    # Проверяем, что элементы внутри — это обычные словари
    assert isinstance(result[0], dict)


@patch("builtins.open", side_effect=FileNotFoundError)
def test_transactions_csv_file_not_found(mock_builtin_open):
    """Тест поведения функции, если файл не найден."""

    # Проверяем, что функция прокидывает ошибку FileNotFoundError наружу
    with pytest.raises(FileNotFoundError):
        transactions_csv("non_existent_file.csv")