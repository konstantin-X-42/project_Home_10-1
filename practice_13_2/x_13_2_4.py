"""
1. Метод finditerpythonpattern.finditer(string, pos=0, endpos=inf)
метод ищет все вхождения шаблона в строке string. Возвращает итератор.
"""

import re

# Компиляция регулярного выражения
pattern = re.compile(r"\d+")

# Поиск всех чисел в строке
text = "There are 2 apples and 5 bananas"
matches = pattern.finditer(text)

# Строка matches = pattern.finditer(text) - в такой конструкции это ИТЕРАТОР
# находит в тексте все места, подходящие под правило,
# но не загружает их в память целиком (в отличие от списка). Она просто создаёт «указатель»,
# готовый выдавать совпадения.


for match in matches:
    print(match)

# строка for match in matches:
# запускает цикл, который по очереди достаёт из итератора matches каждое найденное совпадение.

# >>> <re.Match object; span=(10, 11), match='2'>
# >>> <re.Match object; span=(23, 24), match='5'>


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  -- 2. Метод --  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
2. Метод fullmatchpythonpattern.fullmatch(string, pos=0, endpos=inf)
метод проверяет, соответствует ли вся строка шаблону.
Возвращает объект match или None, если ничего не найдено.
"""

# import re

# Компиляция регулярного выражения
pattern = re.compile(r"\d{4}")  # ищем 4 числа подряд

# Проверка соответствия всей строки шаблону
text = "2024"
match = pattern.fullmatch(text)  # type: ignore
print(match)

# >>> <re.Match object; span=(0, 4), match='2024'>


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  -- 3. Метод --  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
3. Метод splitpythonpattern.split(string, maxsplit=0)
метод разделяет строку string на список, использует шаблон pattern в качестве разделителя.
"""

# import re

# Компиляция регулярного выражения
pattern = re.compile(r"\s+")

# Разделение строки по пробелам
text = "Split this sentence into words"
split_text = pattern.split(text)
print(split_text)

# >>> ['Split', 'this', 'sentence', 'into', 'words']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  -- 4. Метод --  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
4. Метод subnpythonpattern.subn(repl, string, count=0)
Используйте код с осторожностью.Этот метод заменяет все вхождения шаблона pattern на строку repl в строке string.
Возвращает кортеж, содержащий измененную строку и количество замен.
"""

# import re

# Компиляция регулярного выражения
pattern = re.compile(r"\d+")

# Замена всех чисел на слово 'number'
text = "I have 2 apples and 5 bananas"
new_text, num_subs = pattern.subn("number", text)

# Перед знаком равно указаны два значения, потому что метод subn() возвращает кортеж (tuple) из двух элементов.
# В Python это распаковка кортежа (tuple unpacking).
# Он позволяет сразу разложить элементы из возвращаемой структуры по отдельным переменным.

print(new_text)
print(num_subs)

# >>> I have number apples and number bananas
# >>> 2


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  -- 5. Метод --  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
5. Параметры endpos и pos
   endpos и pos — используются в методах: search, match, fullmatch, findall и finditer
   для указания части строки, в которой нужно искать совпадения.
     - pos — начальная позиция (индекс) в строке, с которой начинается поиск.
     - endpos — конечная позиция (индекс) в строке, до которой продолжается поиск.
"""

# import re

# Компиляция регулярного выражения
pattern = re.compile(r"\d+")

# Строка для поиска
text = "123abc456"

# Поиск числа, начиная с индекса 3 и до индекса 8
match = pattern.search(text, pos=3, endpos=8)  # type: ignore  # возвращает вхождение цифр от 3 по 8 эл
print(match)

# >>> <re.Match object; span=(6, 8), match='45'>

# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  -- 6. Метод --  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
6. Параметр maxsplitmaxsplit — этот параметр используется в методе split для указания максимального
количества разделений, которые нужно сделать. Если maxsplit равен 0, то количество разделений не ограничено.
"""

# import re

# Компиляция регулярного выражения
pattern = re.compile(r"\s+")

# Строка для разделения
text = "Split this sentence into words"

# Разделение строки по пробелам, но максимум на 2 части
split_text = pattern.split(text, maxsplit=2)  # выводим строку с 2-я разделениями
print(split_text)

# >>> ['Split', 'this', 'sentence into words']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  -- 7. Метод --  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
7. Параметры repl и countrepl и count — эти параметры используются в методах sub и subn для замены совпадений
    - .repl — строка или функция, на которую нужно заменить совпадения
    - .count — максимальное количество замен. Если count равен 0, то заменяются все совпадения.
"""

# import re

# Компиляция регулярного выражения
pattern = re.compile(r"\d+")

# Строка для замены
text = "I have 2 apples and 5 bananas"

# Замена всех чисел на слово 'number', но максимум 1 замена
new_text = pattern.sub("number", text, count=1)
print(new_text)

# >>> I have number apples and 5 bananas


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  -- 8. Метод --  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
8. Задача
Напишите программу, которая будет извлекать даты из списка строк и преобразовывать их в единый формат YYYY–MM–DD.
Даты могут быть представлены в различных форматах, например DD/MM/YYYY, MM–DD–YYYY, YYYY.MM.DD.
"""

# import re

# Регулярные выражения для различных форматов дат
patterns = [
    re.compile(r"(\d{2})/(\d{2})/(\d{4})"),  # Формат DD/MM/YYYY
    re.compile(r"(\d{2})-(\d{2})-(\d{4})"),  # Формат MM-DD-YYYY
    re.compile(r"(\d{4})\.(\d{2})\.(\d{2})"),  # Формат YYYY.MM.DD
]


def normalize_date(date_str):  # type: ignore
    """
    2. функция проверяет даты и обрабатывает по заданным паттернам, приводит в один вид YYYY-MM-DD
    """
    for patt in patterns:
        mat = patt.search(date_str)
        if mat:
            # print(match)
            # print(match.group())
            if patt.pattern == r"(\d{2})/(\d{2})/(\d{4})":  # DD/MM/YYYY to YYYY-MM-DD
                return f"{mat.group(3)}-{mat.group(2)}-{mat.group(1)}"
            elif patt.pattern == r"(\d{2})-(\d{2})-(\d{4})":  # MM-DD-YYYY to YYYY-MM-DD
                return f"{mat.group(3)}-{mat.group(1)}-{mat.group(2)}"
            elif patt.pattern == r"(\d{4})\.(\d{2})\.(\d{2})":  # YYYY.MM.DD to YYYY-MM-DD
                return f"{mat.group(1)}-{mat.group(2)}-{mat.group(3)}"
    return None


def extract_and_normalize_dates(strings):  # type: ignore
    """1. функция принимает список, возвращает тот же список с преобразованным форматом дат: YYYY-MM-DD"""
    normalized_dates = []
    for string in strings:
        normalized_date = normalize_date(string)  # type: ignore
        if normalized_date:
            normalized_dates.append(normalized_date)
    return normalized_dates


# ИНИЦИАЛИЗИРУЕМ программу из 2-х ФУНКЦИЙ
# Пример списка строк с датами
dates = [
    "Сегодня 23/04/2021",
    "Встреча назначена на 12-05-2020",
    "Событие произошло 2019.06.17",
    "Дата: 15/08/2022, запомните её!",
    "Запланировано на 07-31-2023",
]

# Извлекаем и нормализуем даты
print(extract_and_normalize_dates(dates))  # type: ignore

# >>> ['2021-04-23', '2020-12-05', '2019-06-17', '2022-08-15', '2023-07-31']
