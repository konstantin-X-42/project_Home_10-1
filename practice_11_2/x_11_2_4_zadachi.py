import time

"""
Задача 1
Напишите декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией,
являются целыми, и округляет их до целых, если это не так.
"""
print("-- Задача 1 --")


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
print("-- Задача 2 --")
# import time


def retry(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                time.sleep(3)
        raise Exception("Вызов функции завершился неудачей после нескольких попыток.")

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

"""
Задача 3
Напишите декоратор, который позволяет возвращать элементы декорируемой функции по одному через yield,
если эта функция возвращает список или кортеж.
"""
print("-- Задача 3 --")


def yield_items(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        result = func(*args, **kwargs)
        # Проверка на тип с использованием type()
        # if type(result) in (list, tuple):
        if isinstance(result, (list, tuple)):  # Действие, если это список или кортеж
            for item in result:
                yield item
        else:
            yield result

    return wrapper


# запускаем декоратор — вешаем над функцией
@yield_items
# def yield_items_result():
def get_data(n):  # type: ignore
    if n > 0:
        return [1, 2, 3]  # Возвращаем список
    else:
        return "Одиночный объект"  # Возвращаем строку


# Теперь функция get_data стала генератором!

# ЗАПУСК:
# Просто вызвать get_data(5) недостаточно, так как это теперь генератор.
# Нужно пройтись по нему циклом или превратить в список.

print("--- Результат для списка ---")
for x in get_data(5):
    print(x)

print("\n--- Результат для строки ---")
for x in get_data(-1):
    print(x)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
