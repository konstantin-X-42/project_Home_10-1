from functools import wraps

import pytest

"""
КАМАНДА ЗАПУСКАЕТ ТЕСТ в консоль МОДУЛЬ x_11_2_8_zadachi
pytest practice_11_2/x_11_2_7_TESTI_s_pytest_video.py
"""

"""
Тестирование декораторов без параметров
"""


def double_decorator(func):  # type: ignore
    """Декоратор возвращает результат любой функции умноженный на 2"""

    def wrapper(*args, **kwargs):  # type: ignore
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


# import pytest


def test_double_decorator():  # type: ignore
    """Тестируем сам декоратор, а не результат функции и не как оборачивает функцию"""

    @double_decorator
    def add_numbers(a, b):  # type: ignore
        """Используем любую функцию, возвращающую числовые значения, результат должен умножен на 2"""
        return a + b

    result = add_numbers(3, 5)
    assert result == 16  # (3 + 5) * 2


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Тестирование декораторов с параметрами
"""


def retry_decorator(max_retries):  # type: ignore
    """Декоратор осуществляет заданное количество попыток отправки, в случае не удачи выкидывает исключение"""

    def decorator(func):  # type: ignore
        """Тестируем сам декоратор на правильность обработки исключения, функция тестируется отдельно"""

        def wrapper(*args, **kwargs):  # type: ignore
            for _ in range(max_retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Retrying... ({e})")
            raise Exception("Превышено максимальное количество попыток")

        return wrapper

    return decorator


@retry_decorator(max_retries=3)  # type: ignore  # количество попыток
def example_function():  # type: ignore
    """используем любую функцию, которая возвращает ошибку"""
    raise ValueError("Что-то пошло не так!")  # функция всегда возбуждает ошибку


# import pytest
# Тест декоратора
def test_retry_decorator():  # type: ignore
    """Проверка декоратора на обработку исключения"""
    with pytest.raises(
        Exception, match="Превышено максимальное количество попыток"
    ):  # обрабатываем исключение декоратора
        example_function()


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# from functools import wraps

"""
Написать тесты дя декоратора check_that_arg_is
"""


def check_that_arg_is(predicate, error_message):  # type: ignore
    """Декоратор проверяет аргументы функции на соответствие определенному правилу (предикату)
    Если всё хорошо, декоратор вызывает оригинальную функцию function(arg) и возвращает её результат.
    Если проверка провалена (if not predicate(arg)), он не пускает код дальше и «выбрасывает» ошибку ValueError
    @wraps(function): передаёт документацию оригинальной функции при вызове из функции обертки"""

    def wrapper(function):  # type: ignore
        @wraps(function)
        def inner(arg):  # type: ignore
            if not predicate(arg):
                raise ValueError(error_message)
            return function(arg)

        return inner

    return wrapper


def predicate_is_int(x):  # type: ignore
    """функция-предикат проверяет переданное значение - целое число, возвращает результат"""
    return isinstance(x, int)  # то же type(x) == int


def predicate_is_positive(x):  # type: ignore
    """функция-предикат проверяет переданное значение больше нуля, возвращает результат"""
    return x > 0


# """вызов декоратора с аргументами для предиката predicate_is_int"""
@check_that_arg_is(predicate_is_int, "Значение должно быть целым числом")  # type: ignore
# """вызов декоратора с аргументами для предиката predicate_is_positive"""
@check_that_arg_is(predicate_is_positive, "Число должно быть положительным")  # type: ignore
def square(x):  # type: ignore
    """Функция возводит числа в квадрат"""
    return x * x


# Тест декоратора с функцией-предикат
if __name__ == "__main__":  # конструкция для местного вызова кода

    with pytest.raises(ValueError, match="Число должно быть положительным"):
        """Достаточно одной проверки предиката обвёрнута декоратором, проверяем исключение декоратора ValueError"""
        square(-3)  # передаём в функцию-предикат значение вызывающее ошибку

    # Тесты к декоратору не относятся тестирование функции
    assert square(2) == 4  # проверка функции на правильность работы
    assert predicate_is_positive(3)  # type: ignore # проверка функции-предикат assert predicate_is_positive(3) == True
