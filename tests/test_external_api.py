import unittest
from unittest.mock import MagicMock, patch

import requests

from external_api import convert_to_rub


class TestExternalApi(unittest.TestCase):

    @patch("external_api.requests.get")
    def test_convert_to_rub_usd(self, mock_get: MagicMock) -> None:
        """Тест успешной конвертации USD в RUB."""
        # Настройка mock-ответа от API
        mock_response = MagicMock()
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_get.return_value = mock_response

        transaction = {"amount": 100.0, "currency": "USD"}
        result = convert_to_rub(transaction)

        # Проверка результата и вызова API
        self.assertEqual(result, 7500.0)
        self.assertIsInstance(result, float)
        mock_get.assert_called_once_with(
            "https://apilayer.com", headers={"apikey": unittest.mock.ANY}, params={"symbols": "RUB", "base": "USD"}
        )

    @patch("external_api.requests.get")
    def test_convert_to_rub_eur(self, mock_get: MagicMock) -> None:
        """Тест успешной конвертации EUR в RUB."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"rates": {"RUB": 85.0}}
        mock_get.return_value = mock_response

        transaction = {"amount": "50.5", "currency": "EUR"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 4292.5)
        self.assertIsInstance(result, float)

    @patch("external_api.requests.get")
    def test_convert_to_rub_already_rub(self, mock_get: MagicMock) -> None:
        """Тест транзакции в RUB (API не должно вызываться)."""
        transaction = {"amount": 1500.0, "currency": "RUB"}
        result = convert_to_rub(transaction)

        self.assertEqual(result, 1500.0)
        mock_get.assert_not_called()

    @patch("external_api.requests.get")
    def test_convert_to_rub_api_error(self, mock_get: MagicMock) -> None:
        """Тест генерации исключения при ошибке сети запроса."""
        mock_get.side_effect = requests.RequestException("Ошибка сети")

        transaction = {"amount": 10.0, "currency": "USD"}

        with self.assertRaises(RuntimeError):
            convert_to_rub(transaction)

    def test_convert_to_rub_invalid_currency(self) -> None:
        """Тест генерации исключения при неподдерживаемой валюте."""
        transaction = {"amount": 100.0, "currency": "GBP"}

        with self.assertRaises(ValueError):
            convert_to_rub(transaction)


if __name__ == "__main__":
    unittest.main()

# --------------------------------------------------------------------


# # Загружаем переменные окружения из .env в корне проекта
# env_path = Path(__file__).resolve().parent.parent / ".env"  # библиотека pathlib вычисляется точный путь до
# файла .env
# load_dotenv(dotenv_path=env_path)  # открывает и читает файл .env и делает доступным для Python
#
# # print("Проверка ключа:", os.getenv("CURRENCY_API_KEY"))
#
# API_KEY = os.getenv("CURRENCY_API_KEY")
# BASE_URL = "https://apilayer.com"
#
#
# def conversion_rub(amount: float, from_currency: str) -> float:
#     """Конвертирует сумму из указанной валюты (USD/EUR) в RUB через API.
#
#     Если API недоступно или ключ отсутствует, возвращает 0.0.
#     """
#     if not API_KEY:
#         print("Ошибка: API-ключ не найден в переменных окружения.")
#         return 0.0
#
#     headers = {"apikey": API_KEY}
#     params = {"to": "RUB", "from": from_currency, "amount": amount}
#
#
# # print(conversion_rub(102.53, "USD"))
# # print(conversion_rub(102.53, "RUB"))
