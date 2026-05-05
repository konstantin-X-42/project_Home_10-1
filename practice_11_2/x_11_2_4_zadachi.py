import time

"""
Задача 1
Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
являются целыми, и округляет их до целых, если это не так.
"""


def check_integers(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        if isinstance(result, float):  # та же, но правильная запись if type(result) == float:
            return round(result)
        elif type(result) in (list, tuple):
            rounded = [round(x) if isinstance(x, float) else x for x in result]  # изменил type(x) == float
            # Возвращаем тот же тип, что и исходный (list или tuple)
            return type(result)(rounded)
        else:
            return result

    return wrapper


# запускаем декоратор — вешаем над функцией
@check_integers
def multiply(a, b):  # type: ignore
    return a * b


# Вызываем обычную функцию, а декоратор сработает сам
res_1 = multiply(2, 2.6)  # 2 * 2.6 = 5.2. Декоратор округлит до 5
res_2 = multiply(10, 2)  # 20. Декоратор просто вернет 20

print(res_1)
print(res_2)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 2
Напишите декоратор, который повторно вызывает декорируемую функцию три раза.
Каждый раз через три секунды, если произошла ошибка.
"""

# import time


def retry(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                time.sleep(3)
        raise Exception("Function call failed after multiple retries.")

    return wrapper


# запускаем декоратор — вешаем над функцией
@retry
def unstable_function():  # type: ignore
    print("Пробую выполнить действие...")
    # Имитируем ошибку для проверки
    raise ValueError("Ой, что-то пошло не так!")


# Вызов:
try:
    unstable_function()
except Exception as e:
    print(f"Итог: {e}")

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
