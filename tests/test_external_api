import unittest
from unittest.mock import patch, MagicMock
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
            "https://apilayer.com",
            headers={"apikey": unittest.mock.ANY},
            params={"symbols": "RUB", "base": "USD"}
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
