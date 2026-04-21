import pytest

from src.widget import mask_account_card  # , get_date


# параметризация теста все пишется в модуле test_... (conftest.py только для фикстур)
@pytest.mark.parametrize(
    "input_string, expected_result",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "7158 30** **** 6758"),
        ("Visa Classic 6831983878705199", "6831 98** **** 5199"),
        ("Visa Platinum 8990922113665229", "8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "5999 41** **** 6353"),
        ("Счет 64686473678894779589", "** 9589"),
        ("Счет 35383033474447895560", "** 5560"),
        ("Счет 73654108430135874305", "** 4305"),
    ],
)
def test_correct_get_mask_card_number(input_string, expected_result):
    assert mask_account_card(input_string) == expected_result
