from unittest.mock import Mock, patch

import pytest

from practice_12_1.x_12_1_11_zadachi import get_currency_rate

"""
КАМАНДА ЗАПУСКАЕТ ТЕСТ в консоль из МОДУЛЯ test_x_12_1_11_zadacha_2.py
pytest tests/test_practice_12_1/test_x_12_1_11_zadacha_1.py

подробный тест
pytest -v tests/test_practice_12_1/test_x_12_1_11_zadacha_2.py
"""


def test_get_currency_rate_success():
    """проверяем соответствует ли, результат вывода с подменной URL"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"Valute": {"USD": {"Value": 73.5}}}

    with patch("requests.get", return_value=mock_response):
        result = get_currency_rate("USD")
        assert result == {"currency_code": "USD", "rate": 73.5}


def test_get_currency_rate_no_currency():
    """проверяем функция выводит ошибку ValueError - 'Нет данных по валюте'"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"Valute": {"EUR": {"Value": 89.5}}}

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Нет данных по валюте"):
            get_currency_rate("USD")


def test_get_currency_rate_failed_request():
    """проверяем функция выводит ошибку ValueError - 'Не удалось получить курс валюты'"""
    mock_response = Mock()
    mock_response.status_code = 500

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить курс валюты"):
            get_currency_rate("USD")
