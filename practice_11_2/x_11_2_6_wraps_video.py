from functools import wraps


def wrapped(function):  # type: ignore
    @wraps(function)
    def inner(arg):  # type: ignore
        return function(arg)

    return inner


def foo(_):  # type: ignore  # всегда выдаёт 42
    return 42


print(foo("привет"))  # type: ignore  # Выведет 42
print(foo(100500))  # type: ignore  # Выведет 42


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# from functools import wraps

"""
Настроить декоратор check_that_arg_is на сохранение метаданных о декорируемой функции
"""


def check_that_arg_is(predicate, error_message):  # type: ignore
    def wrapper(function):  # type: ignore
        @wraps(function)  # пробрасывает документацию (метаданные) оригинальной функции в функцию-декаратор
        def inner(arg):  # type: ignore
            if not predicate(arg):
                raise ValueError(error_message)
            return function(arg)

        return inner

    return wrapper


def predicate_is_int(x):  # type: ignore
    return isinstance(x, int)  # тоже :type(x) == int


def predicate_is_positive(x):  # type: ignore
    return x > 0


@check_that_arg_is(predicate_is_int, "Значение должно быть целым числом")  # type: ignore
@check_that_arg_is(predicate_is_positive, "Число должно быть положительным")  # type: ignore
def square(x):  # type: ignore
    """
    Возведение числа в квадрат
     Args:
        x (int): Положительное целое число.
    Returns:
        int: Квадрат числа x.
    Raises:
        ValueError: Если x не является целым или положительным числом.
    """
    return x * x


print(help(square))  # type: ignore  # выводим справочную информацию по функции square, None - выводит функция print()
help(square)
