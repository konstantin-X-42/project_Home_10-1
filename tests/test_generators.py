from src.generators import card_number_generator, filter_by_currency


def test_filter_by_currency_usd(sample_transactions):
    """Проверка фильтрации по USD (должно найти 2 записи)"""
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 3
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert result[2]["id"] == 895315941


def test_filter_by_currency_empty_result(sample_transactions):
    """Проверка, если транзакции в заданной валюте отсутствуют"""
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
    assert len(result) == 3


# --------------------------------------------------------------------


# --------------------------------------------------------------------


def test_card_number_generator_format():
    """Проверяем формат XXXX XXXX XXXX XXXX"""
    generator = card_number_generator(1, 1)
    result = next(generator)
    assert result == "0000 0000 0000 0001"
    assert len(result) == 19  # 16 цифр + 3 пробела


def test_card_number_generator_range():
    """Проверяем генерацию на заданный диапазон (от 10 до 12)"""
    result = list(card_number_generator(10, 12))
    expected = ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]
    assert result == expected
    assert len(result) == 3


def test_card_number_generator_boundaries():
    """Проверка крайних значений (обработка больших чисел)"""
    start_number = 9999999999999998
    end_number = 9999999999999999
    result = list(card_number_generator(start_number, end_number))

    assert result[0] == "9999 9999 9999 9998"
    assert result[1] == "9999 9999 9999 9999"
