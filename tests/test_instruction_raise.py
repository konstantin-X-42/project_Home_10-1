import pytest

from practice_10_2.instruction_raise import calculate_logarithm


def test_calculate_logarithm() -> None:
    assert calculate_logarithm(8, 2) == 3.0
    assert calculate_logarithm(8, 4) == 1.5
    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)
    with pytest.raises(ValueError):
        calculate_logarithm(8, 0)
