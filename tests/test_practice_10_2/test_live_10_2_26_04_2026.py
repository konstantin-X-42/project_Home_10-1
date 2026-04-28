import pytest

from practice_10_2.live_10_2_26_04_2026 import calculate_taxes


def test_calculate_taxes():
    res = calculate_taxes([100, 200, 300], 10)
    assert res == [110, 220, 330]


# *********2**********
# запускаем тест проходит
# *******************


def test_calculate_taxes_2():
    res_1 = calculate_taxes([100, 200, 300], 10)
    res_2 = calculate_taxes([400, 500, 600], 10)
    res_3 = calculate_taxes([700, 800, 900], 10)

    assert res_1 == [110.0, 220.0, 330.0]
    assert res_2 == [440.0, 550.0, 660.0]
    assert res_3 == [770.0, 880.0, 990.0]


# #*********4**********
# #запускаем тест проходит
# #*******************


@pytest.mark.parametrize(
    "price, tax, result",
    [
        ([100, 200, 300], 10, [110, 220, 330]),
        ([100, 200, 300], 10, [110, 220, 330]),
        ([100, 200, 300], 10, [110, 220, 330]),
    ],
)
def test_calculate_taxes_3(price, tax, result):
    res_1 = calculate_taxes(price, tax)
    assert res_1 == result


# #*********5**********
# #запускаем тест проходит
# #*******************


def test_calculate_taxes_zero_2():
    res = calculate_taxes([100, 200, 300], 0)
    assert res == [100, 200, 300]
    # prices = [10, 20, 30]


# *********6**********
# запускаем тест проходит
# *******************


def test_calculate_taxes_zero_3():
    res = calculate_taxes([100, 200, 300], 0)
    assert res == [100, 200, 300]
    # prices[0] = 10


# *********7**********
# запускаем тест проходит
# *******************


def test_calculate_taxes_zero_4():
    prices = [100, 200, 300]
    res = calculate_taxes([100, 200, 300], 0)
    assert res == prices


# *********8**********
# запускаем тест проходит
# *******************


def test_calculate_taxes_zero():
    res = calculate_taxes([100, 200, 300], 0)
    assert res == [100, 200, 300]


def test_calculate_taxes_negative_tax():
    with pytest.raises(ValueError, match="Неверный налоговый процент"):
        calculate_taxes([100, 200, 300], -1)


# *********3**********
# запускаем тест проходит
# *******************


def test_calculate_taxes_negative_price():
    with pytest.raises(ValueError, match="Неверная цена"):
        calculate_taxes([-100, -200, 300], 10)
