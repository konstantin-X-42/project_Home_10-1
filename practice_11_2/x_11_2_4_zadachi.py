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
        if isinstance(result, (list, tuple)):  # Действие, если это список или кортеж
            for item in result:
                yield item
        else:
            yield result

    return wrapper


# запускаем декоратор — вешаем над функцией
@yield_items
def get_data(n):  # type: ignore  # функция get_data стала генератором!
    if n > 0:
        return [1, 2, 3]  # Возвращаем список
    else:
        return "Одиночный объект"  # Возвращаем строку


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

"""
Задача 4
Напишите декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
в котором каждое слово сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка.
"""
print("-- Задача 4 --")


def shorten_words(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        result = func(*args, **kwargs)
        words = result.split()  # преобразуем в список строк ['1', '2', '3']
        shortened_words = []
        for word in words:
            if len(word) > 8:  # определяем str более 8 символов
                shortened_word = word[:8] + "."  # обрезаем до 8 символов и добавляем точку
                shortened_words.append(shortened_word)  # добавляем элемент в конец списка []
            else:
                shortened_words.append(word)  # добавляем элемент в конец списка []
        return " ".join(shortened_words)

    return wrapper


@shorten_words
def get_text():  # type: ignore
    return "программирование"


print(get_text())


# запись кода в одну строку
def shorten_words_2(func):  # type: ignore
    def wrapper(*args, **kwargs):  # type: ignore
        result = func(*args, **kwargs)
        return " ".join(f"{word_2[:8]}." if len(word_2) > 8 else word_2 for word_2 in result.split())

    return wrapper


@shorten_words_2
def get_text_2():  # type: ignore
    return "программирование_2"


print(get_text_2())
