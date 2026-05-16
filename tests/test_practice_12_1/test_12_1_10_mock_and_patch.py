from typing import Any
from unittest.mock import patch

import requests


# 1. функцию пишем здесь, чтобы она гарантированно вызывала requests.get
def get_weather_local(latitude: float, longitude: float) -> float:
    """Получение температуры по координатам, прописываем локально API=None"""
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=None&units=metric"
    )
    data: dict[str, Any] = response.json()
    return float(data["main"]["temp"])


# 2. тест
@patch("requests.get")
def test_get_weather(mock_get):

    mock_get.return_value.json.return_value = {"main": {"temp": 1}}

    # Запускаем функцию (теперь она точно вызовет requests.get)
    result = get_weather_local(1, 1)

    # Проверяем возвращаемое значение
    assert result == 1

    # Проверяем, что вызов в интернет был перехвачен ровно 1 раз
    assert mock_get.call_count == 1
