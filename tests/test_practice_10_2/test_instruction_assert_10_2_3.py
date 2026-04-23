import pytest

from practice_10_2.instruction_assert_10_2_3 import add, add_numbers, divide, find_max, is_even, multiply, subtract


def test_add_numbers() -> None:
    assert add_numbers(2, 3) == 5


def test_is_even() -> None:
    assert is_even(4) is True
    assert is_even(3) is False


def test_find_max() -> None:
    assert find_max([1, 5, 3, 8, 2]) == 8


# ----------------------------------------------------- +


# Тест функции сложения
def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(0, 0) == 0


# Тест функции вычитания
def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-2, 3) == -5
    assert subtract(0, 0) == 0


# Тест функции умножения
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 0) == 0


# Тест функции деления
def test_divide():
    assert divide(6, 2) == 3
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)
