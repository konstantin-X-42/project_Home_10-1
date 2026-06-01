import random
import re
import string
from collections import Counter, defaultdict, deque

"""
1. ЗАДАЧА
Напишите программу, которая находит все даты в формате "dd-mm-yyyy" в заданном тексте.
"""

# import re

text = "Сегодня 23-09-2021, а завтра будет 24-09-2021. Вчера была дата 22-09-2021."

pattern = r"\b\d{2}[-]\d{2}[-]\d{4}\b"

dates = re.findall(pattern, text)

print(dates)

# >>> ['23-09-2021', '24-09-2021', '22-09-2021']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
2. ЗАДАЧА
Напишите программу, которая извлекает все хештеги из заданного текста.
"""
# import re

text = "Сегодня я сделал #Python, а вчера #MachineLearning. Завтра буду изучать #DataScience."

pattern = r"#\w+"

hash_tags = re.findall(pattern, text)

print(hash_tags)

# >>> ['#Python', '#MachineLearning', '#DataScience']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
3. ЗАДАЧА
Напишите программу, которая проверяет строки на соответствие требованиям пароля:
длина не менее 8 символов, наличие хотя бы одной большой буквы, одной маленькой
буквы и одной цифры.
"""
# import re

passwords = ["Password123", "password", "PASSWORD123", "Passw0rd", "Passw"]

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

valid_passwords = [pwd for pwd in passwords if re.match(pattern, pwd)]

print(valid_passwords)

# >>> ['Password123', 'Passw0rd']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
4. ЗАДАЧА
Напишите программу, которая подсчитывает, сколько раз каждое слово
встречается в тексте. Используйте collections.Counter.
"""
# from collections import Counter

text = "это пример текста в котором встречаются слова и слова могут повторяться слова"

words_list = text.split()

words_counter = Counter(words_list)

print(words_counter)

# >>> Counter({'слова': 3, 'это': 1, 'пример': 1, 'текста': 1, 'в': 1, 'котором': 1,
# 'встречаются': 1, 'и': 1, 'могут': 1, 'повторяться': 1})


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
5. ЗАДАЧА
Используйте defaultdict, чтобы создать словарь, где значения по
умолчанию будут равны пустым спискам. Затем добавьте несколько
ключей и значений в этот словарь.
"""
# from collections import defaultdict

def_dict = defaultdict(list)

data = [("группа1", "элемент1"), ("группа1", "элемент2"), ("группа2", "элемент1")]

for key, val in data:
    def_dict[key].append(val)

print(def_dict)

# >>> defaultdict(<class 'list'>, {'группа1': ['элемент1', 'элемент2'], 'группа2': ['элемент1']})


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
6. ЗАДАЧА
Используйте collections.deque для реализации очереди задач.
Добавьте несколько задач в начало и конец очереди, затем извлеките их.
"""
# from collections import deque

task_deque = deque()  # type: ignore

task_deque.append("Task1")
# 1
task_deque.appendleft("Task2")
# 2 1
task_deque.append(("Task3"))
# 2 1 3
task_deque.appendleft("Task4")
# 4 2 1 3
task_deque.append("Task5")
# 4 2 1 3 5

while task_deque:
    print(task_deque.popleft())

# >>> Task4
# >>> Task2
# >>> Task1
# >>> Task3
# >>> Task5


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
7. ЗАДАЧА
Напишите программу, которая создает случайный пароль длиной 12
символов, используются буквы верхнего и нижнего регистра, цифры и специальные символы.
"""
# import random
# import string

all_symbols = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(all_symbols) for _ in range(12))

print(password)

# >>> K>lLt0B(%+d~
# >>> _T9#hUL#D5$f
# >>> FdqP;)Xo(S&\
# >>> O`Ep?h3@V@@2
# >>> (d}W]ZN/++l"
# >>> 5ym1a%FYG7'O


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
8. ЗАДАЧА
Создайте список чисел от 1 до 10 и перемешайте его элементы случайным образом.
"""
# import random

numbers_list = list(range(1, 11))

random.shuffle(numbers_list)

print(numbers_list)

# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> [7, 4, 2, 8, 5, 9, 6, 1, 10, 3]
# >>> [9, 2, 3, 4, 5, 10, 1, 6, 8, 7]
# >>> [3, 2, 9, 1, 4, 8, 7, 6, 5, 10]
# >>> [6, 9, 5, 4, 8, 1, 3, 2, 10, 7]
# >>> [7, 10, 6, 4, 2, 9, 1, 5, 8, 3]
# >>> [1, 7, 2, 10, 3, 8, 6, 9, 4, 5]
# >>> [3, 7, 5, 8, 2, 1, 10, 9, 4, 6]
# >>> [2, 7, 9, 6, 3, 8, 5, 10, 1, 4]


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --

"""
9. ЗАДАЧА
Дан список студентов. Напишите программу, которая случайным образом
выбирает одного студента для ответа на вопрос.
"""
# import random

students = ["Алексей", "Иван", "Мария", "Ольга", "Екатерина"]

print(random.choice(students))

# >>> Екатерина
# >>> Иван
# >>> Ольга
# >>> Мария
# >>> Екатерина
# >>> Иван
# >>> Иван
# >>> Екатерина
