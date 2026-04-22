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
