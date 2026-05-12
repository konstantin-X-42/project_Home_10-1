import time
from functools import wraps

"""
Задача 1
Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
являются целыми, и округляет их до целых, если это не так. Декоратор должен принимать параметр
precision, который указывает, до скольких цифр после запятой округлять числа.
"""
print("-- Задача 1 --")


# декоратор
def check_floats(precision):  # type: ignore
    def decorator(func):  # type: ignore
        @wraps(func)
        #  @wraps(func) копирует все данные (имя, документацию, список аргументов) из оригинальной функции
        # func во внутреннюю функцию
        def inner(*args, **kwargs):  # type: ignore
            result = func(*args, **kwargs)
            if isinstance(result, float):  # Проверка на тип с использованием type(), то же - if type(result) == float:
                return round(result, precision)
            elif type(result) in (list, tuple):
                rounded = [round(x, precision) if isinstance(x, float) else x for x in result]  # if type(x) == float
                return type(result)(rounded)
            else:
                return result

        return inner

    return decorator


"""оборачиваем функцию декоратором"""


# Применяем декоратор: округляем до 2 знаков
@check_floats(2)  # type: ignore
def calculate_price(price, tax):  # type: ignore
    return price * tax


@check_floats(3)  # type: ignore
def get_coordinates():  # type: ignore
    # Работает и со списками/кортежами, как прописано в коде
    return [3.14159, 2.71828, "ошибка"]


# Запуск
print(calculate_price(100.0, 0.0555))  # Выведет: 5.55
print(get_coordinates())  # Выведет: [3.142, 2.718, 'ошибка']

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 2
Напишите декоратор, который повторно вызывает декорируемую функцию заданное количество раз
через заданное время, если произошла ошибка. Параметры, передаваемые в декоратор,
обязательно должны быть именованными.
"""
print("\n-- Задача 2 --")

# from functools import wraps
# import time


# декоратор
def retry(*, retries=3, delay=3):  # type: ignore #  * все аргументы после retries,
    # и delay должны передаваться только по имени.
    def wrapper(func):  # type: ignore
        @wraps(func)
        def inner(*args, **kwargs):  # type: ignore
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    time.sleep(delay)  # метод .sleep(5) - приостановление программы на 5 сек
            raise Exception(
                "Сбой вызова функции после нескольких попыток"
            )  # raise — команда «поднять» (выбросить) ошибку.
            # После неё выполнение обычного кода в этой ветке прекращается.

        return inner

    return wrapper


"""оборачиваем функцию декоратором"""
# функция, «капризничает» и выдает ошибку первые два раза, а на третий — срабатывает


@retry(retries=5, delay=1)  # type: ignore  # Настраиваем: 5 попыток, пауза 1 секунда между ними
def unstable_connection():  # type: ignore
    # Создаем счетчик внутри функции для теста
    if not hasattr(unstable_connection, "attempts"):
        unstable_connection.attempts = (
            0  # unstable_connection - переменная, .attempts — свойство (атрибут) этого объекта,
        )
        # хранится число уже совершенных попыток подключения или повторных запросов.

    unstable_connection.attempts += 1
    print(f"Попытка №{unstable_connection.attempts}...")

    if unstable_connection.attempts < 3:
        raise ValueError("Временная ошибка сети")  # Специально вызываем ошибку
    return "Успех! Данные получены."


# вызываем функцию контролируя исключением ошибки
try:
    result = unstable_connection()
    print(f"Результат: {result}")
except Exception as e:
    print(f"ВНИМАНИЕ: {e}")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 3
Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
в котором каждое слово сокращено до определенной длины. Если слово было сокращено,
в конце слова ставится переданный символ. Количество символов в слове и знак в конце сокращенного слова
— параметры декоратора, причем символ обязательно должен передаваться как именованный аргумент.
"""
print("\n-- Задача 3 --")

# from functools import wraps


# декоратор
def shorten_words(max_len, *, end_symbol="."):  # type: ignore
    def wrapper(func):  # type: ignore
        @wraps(func)
        def inner(*args, **kwargs):  # type: ignore
            result_3 = func(*args, **kwargs)
            return " ".join(
                f"{word[:max_len]}{end_symbol}" if len(word) > max_len else word for word in result_3.split()
            )

        return inner

    return wrapper


"""оборачиваем функцию декоратором"""


@shorten_words(4, end_symbol="!")  # type: ignore
def some_func():  # type: ignore
    return "Впрочем, никого не прельщает сама по себе боль, никто не желает её приобретения\
        \n и не ищет её только потому, что она — боль..."


print(some_func())
# >>> Впро! нико! не прел! сама по себе боль! никт! не жела! её прио! и не ищет её толь! пото! что она — боль!

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 4
Напишите тесты с использованием библиотеки pytest для проверки корректности работы декоратора из задачи 3.
"""
"""
КАМАНДА ЗАПУСКАЕТ ТЕСТ в консоль МОДУЛЬ x_11_2_8_zadachi
pytest practice_11_2/x_11_2_8_zadachi.py
"""
print("\n-- Задача 4 --")
# import pytest


# Тест № 1
# Тестируемая функция
@shorten_words(4, end_symbol="!")  # type: ignore  # задаём параметры
def get_text():  # type: ignore  # запускаем функцию
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit."  # задаём вывод функции


# print(get_text())     # запускаем для визуализации результата декоратора
# >>> Lore! ipsu! dolo! sit amet! cons! adip! elit!


def test_shortening():  # type: ignore
    """проверка декоратора на правильность среза и добавление элемента"""
    assert get_text() == "Lore! ipsu! dolo! sit amet! cons! adip! elit!"
    # сравниваем обработка декоратора = ожидаемый результат


# --------------------------------------------
# Тест № 2
def test_no_shortening():  # type: ignore
    """проверка декоратора на возврат идентичной строки без среза"""

    # увеличиваем допустимые элементы, возврат строки декоратором без изменений
    @shorten_words(10, end_symbol="!")  # type: ignore
    def get_long_text():  # type: ignore
        return "Lorem ipsum dolor sit amet"

    assert get_long_text() == "Lorem ipsum dolor sit amet"


# --------------------------------------------
# Тест № 3
def test_end_symbol():  # type: ignore
    """проверка декоратора, что вставляет символ в конце каждого элемента и не оставляет пробел"""

    @shorten_words(3, end_symbol="?")  # type: ignore
    def get_questioned_text():  # type: ignore
        return "Lorem ipsum dolor"

    assert get_questioned_text() == "Lor? ips? dol?"


# --------------------------------------------
# Тест № 4
def test_different_lengths():  # type: ignore
    """проверка декоратора, на правильность выборочного среза и не оставляет пробел"""

    @shorten_words(5, end_symbol=".")  # type: ignore
    def get_different_lengths_text():  # type: ignore
        return "Hello beautiful world"

    assert get_different_lengths_text() == "Hello beaut. world"
