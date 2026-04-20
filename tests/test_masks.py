from src.masks import get_mask_card_number


def test_correct_number(number_card):
    assert get_mask_card_number("7000792289606361") == number_card
    assert get_mask_card_number(7000792289606361) == number_card


def test_not_correct_number(number_card):
    assert get_mask_card_number("700079228960636") != number_card
    assert get_mask_card_number(700079228960636) != number_card
    assert get_mask_card_number("70007922+9606361") != number_card
    assert get_mask_card_number(70007922 + 9606361) != number_card
    assert get_mask_card_number("70007922889606361") != number_card
    assert get_mask_card_number(70007922889606361) != number_card
    assert get_mask_card_number("h000792289606361") != number_card
    assert get_mask_card_number("-700079228960636") != number_card
    assert get_mask_card_number(-700079228960636) != number_card
    assert get_mask_card_number(["7000792289606361"]) != number_card  # type: ignore
    assert get_mask_card_number([7000792289606361]) != number_card  # type: ignore
    assert get_mask_card_number({"7000792289606361"}) != number_card  # type: ignore
    assert get_mask_card_number({7000792289606361}) != number_card  # type: ignore
    assert get_mask_card_number() != number_card
