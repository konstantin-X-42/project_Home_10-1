"""
ГЕНЕРАТОРНЫЕ ВЫРАЖЕНИЯ
"""

from itertools import chain

# генерирует числа от 0 до 4 возведенные в квадрат
squares = (x * x for x in range(5))
print(list(squares))  # >>> [0, 1, 4, 9, 16]
print(list(squares))  # >>> []  # в генераторе исчерпаны элементы

# генерирует чётные числа от 0 до 9
evens = (x for x in range(10) if x % 2 == 0)
print(list(evens)[2])  # >>> 4  (возвращает значение с индексом два)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 1
Напишите генераторное выражение, которое возвращает кубы четных чисел от 0 до 10.
Решение
"""
cubes = (x**3 for x in range(11) if x % 2 == 0)
print(list(cubes))  # >>> [0, 8, 64, 216, 512, 1000]

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 2
Напишите функцию, которая принимает список чисел и возвращает сумму квадратов положительных
чисел в этом списке. Используйте для этого генераторное выражение.
Решение
"""


def sum_of_squares(lst):  # type: ignore
    return sum(x**2 for x in lst if x > 0)


sum_of_squares([-2, 3, 4])  # type: ignore   # >>> 25

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 3
Напишите генераторное выражение, которое возвращает буквы строки "hello", но только если они являются гласными.
Решение
"""
vowels = (x for x in "hello" if x in ["a", "e", "i", "o", "u"])
print(list(vowels))  # >>> ['e', 'o']

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 4
Найдите среднее арифметическое всех чисел, кратных 3 или 5, в диапазоне от 1 до 100 включительно.
Решение
"""
numbers = range(1, 101)
filtered_numbers = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, numbers))
average = sum(filtered_numbers) / len(filtered_numbers)
print(average)  # >>> 51.4468085106383

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 5
Объедините несколько списков в один список, учитывая возможные дубликаты элементов.
Решение
"""
# from itertools import chain

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]
combined_list = list(set(chain(list1, list2, list3)))
print(combined_list)  # >>> [1, 2, 3, 4, 5, 6, 7, 8]

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Задача 6
Дан список словарей. Отфильтруйте его по ключу age и значению 30.
Решение
"""
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]
filtered_people = list(filter(lambda x: x["age"] == 30, people))
print(filtered_people)  # >>> [{'name': 'Bob', 'age': 30}, {'name': 'David', 'age': 30}]


def simple_generator():  # type: ignore
    yield 1
    yield 2
    yield 3


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

gen = simple_generator()  # type: ignore

print(next(gen))
# >>> 1
print(next(gen))
# >>> 2
print(next(gen))
# >>> 3

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

"""
Генератор в цикле
"""


def simple_generator():  # type: ignore
    yield 1
    yield 2
    yield 3


for value in simple_generator():  # type: ignore
    print(value)
# >>> 1
# >>> 2
# >>> 3

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


def infinite_sequence(start=1):  # type: ignore
    while True:
        yield start
        start += 1


numbers = infinite_sequence()  # type: ignore
print(next(numbers))
# >>> 1
print(next(numbers))
# >>> 2
# …
