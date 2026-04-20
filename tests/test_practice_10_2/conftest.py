import pytest


@pytest.fixture
def number_list():
    """ПРИМЕР фикстуры c функцией "max и sum" для практики 10_2_6"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def numbers():
    """ПРИМЕР фикстуры для практики 10_2_6"""
    return "321"


@pytest.fixture
def letters():
    """ПРИМЕР фикстуры для практики 10_2_6"""
    return "olleh"
