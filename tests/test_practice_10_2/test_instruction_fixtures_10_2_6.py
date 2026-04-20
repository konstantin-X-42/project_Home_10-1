# import pytest

from practice_10_2.instruction_fixtures_10_2_6 import reverse_string


def test_reverse_string(numbers):
    """ПРИМЕР фикстуры для практики 10_2_6"""
    assert reverse_string("123") == numbers


def test_reverse_letters(letters):
    """ПРИМЕР фикстуры для практики 10_2_6"""
    assert reverse_string("hello") == letters
