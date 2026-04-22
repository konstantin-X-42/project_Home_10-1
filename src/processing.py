from typing import Any


def filter_by_state(
    date_list: list[dict[str, Any]] | tuple[dict[str, Any]] | None = None, state: str = "EXECUTED"
) -> Any: #list[dict[str, Any]]:
    """функция возвращает массив с выбранным ключом state по умолчанию возвращает с 'EXECUTED'"""

    try:  # обработка исключений
        if date_list is None:
            return "Error_11 - в функцию не подаются аргументы"
        state_list = []
        for state_dict in date_list:  # итерируем словари из списка (массива)
            if state == state_dict["state"]:
                state_list.append(state_dict)  # добавляем словарь в конец списка каждую итерацию
        return state_list
    except KeyError:  # обращение к элементу словаря (dict) по key, которого в этом словаре нет
        return "Error_12 - в аргументе функции, key в словарях или в одном из словарей отсутствует"
    # except Exception:  # другая непредвиденная ошибка
    #     return []  # "Error_11 - в функцию не подаются аргументы или поданы в ином формате"


# --------------------------------------------------------------------


def sort_by_date(date_list: list[dict[str, Any]] | None = None, reverse: bool = True) -> Any: #list[dict[str, Any]]:
    """функция сортирует словари по дате: на убывание - по умолчанию или на возрастание,
    по установленному значению в аргументе - sorting"""

    try:  # обработка исключений
        if date_list is None:
            return "Error_13 - в функцию не подаются аргументы"
        return sorted(date_list, key=lambda x: x["date"], reverse=reverse)
    except KeyError:  # обращение к элементу словаря (dict) по key, которого в этом словаре нет
        return "Error_14 - в аргументе функции, key в словарях или в одном из словарей отсутствует"
    # except Exception:  # другая непредвиденная ошибка
    #     return []  # "Error_13 - в функцию не подаются аргументы или поданы в ином формате"
