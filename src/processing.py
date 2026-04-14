def filter_by_state(date_list: list[dict] | tuple[dict] = None, state: str='EXECUTED') -> list[dict]:
    """ функция возвращает массив с выбранным ключом state по умолчанию возвращает с 'EXECUTED' """
    try:   # обработка исключений
        state_list = []
        for state_dict in date_list:   # итерируем словари из списка (массива)
            if state == state_dict["state"]:
                state_list.append(state_dict)   # добавляем словарь в конец списка каждую итерацию
        return state_list
    except KeyError:   # обращение к элементу словаря (dict) по key, которого в этом словаре нет
        return "Error_11 - в аргументе функции, key в словарях или в одном из словарей отсутствует"
    except Exception as e:     # другая непредвиденная ошибка
        return "Error_12 - в функцию не подаются аргументы или поданы в ином формате"


# --------------------------------------------------------------------


def sort_by_date(date_list: list[dict] | tuple[dict] = None, reverse: bool=True) -> list[dict]:
    """ функция сортирует словари по дате: на убывание - по умолчанию или на возрастание,
    по установленному значению в аргументе - sorting """
    try:   # обработка исключений
        return sorted(date_list, key=lambda x: x['date'], reverse=reverse)
    except KeyError:   # обращение к элементу словаря (dict) по key, которого в этом словаре нет
        return "Error_13 - в аргументе функции, key в словарях или в одном из словарей отсутствует"
    except Exception as e:     # другая непредвиденная ошибка
        return "Error_14 - в функцию не подаются аргументы или поданы в ином формате"