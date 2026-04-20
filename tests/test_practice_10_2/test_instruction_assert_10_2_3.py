from practice_10_2.instruction_assert_10_2_3 import add_numbers, find_max, is_even


def test_add_numbers() -> None:
    assert add_numbers(2, 3) == 5


def test_is_even() -> None:
    assert is_even(4) is True
    assert is_even(3) is False


def test_find_max() -> None:
    assert find_max([1, 5, 3, 8, 2]) == 8
