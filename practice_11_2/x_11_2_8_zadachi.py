from functools import wraps

"""
Задача 1
Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
являются целыми, и округляет их до целых, если это не так. Декоратор должен принимать параметр
precision, который указывает, до скольких цифр после запятой округлять числа.
"""
print("-- Задача 1 --")

def check_floats(precision):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == float:   # Проверка на тип с использованием type(), то же - if isinstance(result, float):
                return round(result, precision)
            elif type(result) in (list, tuple):
                rounded = [round(x, precision) if type(x) == float else x for x in result]
                return type(result)(rounded)
            else:
                return result
        return inner
    return decorator
