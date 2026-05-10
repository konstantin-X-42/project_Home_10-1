from functools import wraps

"""
Задача 1
Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
являются целыми, и округляет их до целых, если это не так. Декоратор должен принимать параметр
precision, который указывает, до скольких цифр после запятой округлять числа.
"""
print("-- Задача 1 --")


def check_floats(precision):  # type: ignore
    def decorator(func):  # type: ignore
        @wraps(func)
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
import time


def retry(*, retries=3, delay=3):  # type: ignore #  * все аргументы после retries,
    # и delay должны передаваться только по имени.
    def wrapper(func):  # type: ignore
        @wraps(func)
        def inner(*args, **kwargs):  # type: ignore
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except:
                    time.sleep(delay)  # метод .sleep(5) - приостановление программы на 5 сек
            raise Exception(
                "Сбой вызова функции после нескольких попыток"
            )  # raise — команда «поднять» (выбросить) ошибку.
            # После неё выполнение обычного кода в этой ветке прекращается.

        return inner

    return wrapper


"""оборачиваем функцию декоратором"""
"""функция, «капризничает» и выдает ошибку первые два раза, а на третий — срабатывает"""


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
