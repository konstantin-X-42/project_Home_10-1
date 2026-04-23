import pytest

from practice_10_2.instruction_parametrize_10_2_7 import reverse_string


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("hello", "olleh"),
        ("world", "dlrow"),
        ("12345", "54321"),
        ("", ""),
    ],
)  # <<<<< в скобках ("строка в аргумент ф-ии", "ожидаемый результат")
def test_reverse_string(string, expected_result):
    assert reverse_string(string) == expected_result


def test_reverse_string_error():
    # Мы ожидаем, что внутри этого блока возникнет ошибка TypeError
    with pytest.raises(TypeError):
        # Передаем число вместо строки
        reverse_string(12345)  # type: ignore    # <<<<< подавляет визуализацию ошибки
        # (тип передаваемых данных) в строке при проверке анализатором mypy


@pytest.mark.parametrize(
    "input_list, expected_result",
    [
        ([1, 2, 3], [3, 2, 1]),  # Список чисел
        (["a", "b", "c"], ["c", "b", "a"]),  # Список строк
        ([], []),  # Пустой список
    ],
)
def test_reverse_string_with_lists(input_list, expected_result):
    # Условие проверки остается ТАКИМ ЖЕ
    assert reverse_string(input_list) == expected_result
