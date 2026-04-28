from src.generators import filter_by_currency


def test_filter_by_currency_usd(sample_transactions):
    """Проверка фильтрации по USD (должно найти 2 записи)"""
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_empty_result(sample_transactions):
    """Проверка, если такой валюты нет"""
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty_list():
    """Проверка, пустой список транзакций"""
    result = list(filter_by_currency([], "RUB"))
    assert result == []


def test_filter_by_currency_missing_keys(sample_transactions):
    """Проверка, в словаре нет нужных ключей"""
    # Транзакция с id=4 не имеет ключа operationAmount
    result = list(filter_by_currency(sample_transactions, "USD"))
    # Должна пропущена, не вызывая ошибку
    assert len(result) == 2
