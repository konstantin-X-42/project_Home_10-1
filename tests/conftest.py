import pytest


@pytest.fixture
def number_card():
    """маскировка номера карты"""
    return "7000 79** **** 6361"


@pytest.fixture
def number_account():
    """маскировка счёта пользователя"""
    return "** 4305"


@pytest.fixture
def date_str():
    """возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    return "11.03.2024"


@pytest.fixture
def date_list_executed():
    """возвращает массив с выбранным ключом state по умолчанию возвращает с 'EXECUTED'"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def date_list_canceled():
    """возвращает массив с выбранным ключом state по умолчанию возвращает с 'EXECUTED'"""
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def date_list_true():
    """сортирует по дате: на убывание - по умолчанию или на возрастание,
    по установленному значению в аргументе - sorting"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def date_list_false():
    """сортирует по дате: на убывание - по умолчанию или на возрастание,
    по установленному значению в аргументе - sorting"""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def sample_transactions():
    """Генератор, фильтрует транзакции по заданной валюте"""
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "USD Trans"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "RUB Trans"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Another USD Trans"},
        {"id": 4, "description": "No amount info"},  # Тест на пропущенные ключи
    ]
