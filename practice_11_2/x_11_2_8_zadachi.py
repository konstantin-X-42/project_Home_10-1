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
