from collections import Counter, defaultdict

"""
Counter — специальный словарь для подсчета объектов.
"""

# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  1. Counter — специальный словарь  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# подсчёт одинаковых значений списка

# from collections import Counter

# Создаем список
my_list = ["apple", "banana", "apple", "orange", "banana", "banana"]
# Создаем объект Counter на основе списка
counted = Counter(my_list)
# Выводим результаты подсчета
print(counted)

# >>> Counter({'banana': 3, 'apple': 2, 'orange': 1})


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  2. метод most_common()  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# метод most_common() — возвращает список из \(n\) наиболее распространенных элементов и их количество
print(counted.most_common(2))

# >>> [('banana', 3), ('apple', 2)]


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  3. метод elements()  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# метод elements() — возвращает итератор, повторяющий элементы столько раз, сколько указано в их счетчике.
print(list(counted.elements()))

# >>> ['apple', 'apple', 'banana', 'banana', 'banana', 'orange']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  4. метод subtract()  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

# метод subtract() — вычитает элементы из другого итерируемого объекта.
counted.subtract("abbccc")
print(counted)

# >>> Counter({'banana': 3, 'apple': 2, 'orange': 1, 'a': -1, 'b': -2, 'c': -3})


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  5. ЗАДАЧА  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
"""
Задача
Напишите программу, которая принимает на вход список слов и выводит топ-3 самых часто встречающихся
слов в этом списке. Если слова встречаются одинаково часто, их порядок в выводе не важен.
"""
# from collections import Counter

words = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "banana",
    "grape",
    "apple",
    "grape",
    "apple",
]


def get_top_words(list_words: list, top_n: int = 3) -> list:  # type: ignore
    counter_words = Counter(list_words)
    return counter_words.most_common(top_n)


if __name__ == "__main__":
    print(get_top_words(words))


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  6. defaultdict — расширенная версия обычного словаря  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
"""
defaultdict — расширенная версия обычного словаря, который автоматически создает значение
для отсутствующего ключа с использованием функции по умолчанию.
"""
# from collections import defaultdict

# Создаем defaultdict, который возвращает 0 для отсутствующих ключей
my_dict = defaultdict(int)
# Добавляем значение
my_dict["one"] = 1


# Выводим существующее значение
print(my_dict["one"])
# >>> 1

# Выводим значение для отсутствующего ключа
print(my_dict["two"])
# >>> 0


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  7. ЗАДАЧА  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
Напишите программу, которая принимает на вход список пар (имя студента, оценка)
и группирует студентов по оценкам. Программа должна выводить список студентов и их оценок.
"""
# from collections import defaultdict

grades = [("Alice", 85), ("Bob", 90), ("Alice", 95), ("Bob", 85), ("Alice", 88)]


def grades_group(grades_list: list) -> dict:  # type: ignore

    # строка кода создаёт особый тип словаря из модуля collections. Он автоматически создаёт пустой список [],
    # если запрашиваете или изменяете ключ, которого ещё нет в словаре

    names_dict = defaultdict(list)
    for name, grade in grades_list:
        names_dict[name].append(grade)

    return names_dict


if __name__ == "__main__":
    result = grades_group(grades)
    print(result)
