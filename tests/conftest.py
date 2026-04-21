import pytest


@pytest.fixture
def number_card():
    """маскировка номера карты"""
    return "7000 79** **** 6361"


@pytest.fixture
def number_account():
    """маскировка счёта пользователя"""
    return "** 4305"


# @pytest.fixture
# def number_card_02():
#     """маскировка верного номера карты"""
#     return "7000 79** **** 636"

# from src.masks import get_mask_account, get_mask_card_number
# from src.processing import filter_by_state, sort_by_date
# from src.widget import get_date, mask_account_card

# print(get_mask_card_number("7000792289606361")) 1
# print(get_mask_card_number(7000792289606361)) 2
# print(get_mask_card_number("700079228960636")) 3
# print(get_mask_card_number(700079228960636))  4
# print(get_mask_card_number(70007922 + 9606361)) 5
# print(get_mask_card_number("70007922889606361"))
# print(get_mask_card_number(70007922889606361))
# print(get_mask_card_number("h000792289606361"))
# print(get_mask_card_number("-700079228960636"))
# print(get_mask_card_number(-700079228960636))
# print(get_mask_card_number("70007922+9606361"))
# print(get_mask_card_number(["7000792289606361"]))
# print(get_mask_card_number([7000792289606361]))
# print(get_mask_card_number({"7000792289606361"}))
# print(get_mask_card_number({7000792289606361}))
# print(get_mask_card_number())
#
# # ----------------------------------------------
#
# print(get_mask_account("73654108430135874305"))
# print(get_mask_account(73654108430135874305))
# print(get_mask_account("7365410843013587430"))
# print(get_mask_account(7365410843013587430))
# print(get_mask_account(73654108401 + 35874305))
# print(get_mask_account("736541084301358874305"))
# print(get_mask_account(736541084301358874305))
# print(get_mask_account("736g54108430135874305"))
# print(get_mask_account("s3654108430135874305"))
# print(get_mask_account("-3654108430135874305"))
# print(get_mask_account(-73654108430135874305))
# print(get_mask_account("736541084/0135874305"))
# print(get_mask_account(["73654108430135874305"]))
# print(get_mask_account([73654108430135874305]))
# print(get_mask_account({"73654108430135874305"}))
# print(get_mask_account({73654108430135874305}))
# print(get_mask_account())
#
# # ----------------------------------------------
#
# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Счет 35383033474447895560"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Visa Gold 5999414228426353"))
# print(mask_account_card("Счет 73654108430135874305"))
#
# # ----------------------------------------------
#
# print(get_date("2024-03-11T02:26:18.671407"))
# print(get_date("2024-g3-11T02:26:18.671407"))
# print(get_date("2024-33-11T02:26:18.671407"))
# print(get_date("1024-03-11T02:26:18.671407"))
# print(get_date("2024-03-32T02:26:18.671407"))
# print(get_date(20240311022618671407))
# print(get_date())
#
# # ----------------------------------------------
#
# # Пример входных данных для проверки функции
# List_dict_1 = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# print(filter_by_state(List_dict_1))
# print(
#     filter_by_state(
#         (
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         )
#     )
# )
# print(filter_by_state(List_dict_1, "CANCELED"))
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTE", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
# print(
#     filter_by_state(
#         [
#             {"id": 41428829, "stat": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
# print(filter_by_state())
# print(filter_by_state(True))
# print(
#     filter_by_state(
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "id": 615064591,
#             "state": "CANCELED",
#             "date": "2018-10-14T08:21:33.419441",
#         }
#     )
# )
#
# # ----------------------------------------------
#
# # Пример входных данных для проверки функции
# List_dict_2 = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# print(sort_by_date(List_dict_2))
# print(
#     sort_by_date(
#         (
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         )
#     )
# )
# print(sort_by_date(List_dict_2, False))
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "dat": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
# print(sort_by_date())
# print(sort_by_date(False))
# # нет проверки верной даты и времени
# print(
#     sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "45019-25-фига"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
