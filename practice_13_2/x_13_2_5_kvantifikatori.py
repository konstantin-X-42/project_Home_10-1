import re

"""
Квантификаторы, группировка и регулярные выражения
"""

# Квантификаторы — специальные символы, которые определяют,
#                  сколько раз предыдущий символ или символьный класс должен повторяться.


"""
1. Квантификатор *
* — повторение 0 или более раз. Например, a* найдет a, aa, aaa, но также подойдет для пустой строки.python
"""

# import re

text = "aaa abc a ab"
matches = re.findall(r"a*", text)
print(matches)

# >>> ['aaa', '', 'a', '', '', '', 'a', '', 'a', '', '']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  2. Квантификатор +  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
+ — повторение 1 или более раз. Например, a+ найдет a, aa, aaa.
"""
# import re
text = "aaa abc a ab"
matches = re.findall(r"a+", text)
print(matches)

# >>> ['aaa', 'a', 'a', 'a']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  3. Квантификатор ?  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
? — повторение 0 или 1 раз. Например, a? найдет a или пустую строку.
"""
# import re
text = "aaa abc a ab"
matches = re.findall(r"a?", text)
print(matches)

# >>> ['a', 'a', 'a', '', 'a', '', '', '', 'a', '', 'a', '', '']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  4. Квантификатор {n}  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
{n} — повторение ровно n раз. Например, a{2} найдет aa.
"""
# import re
text = "aaa abc a ab"
matches = re.findall(r"a{2}", text)
print(matches)

# >>> ['aa']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  5. Квантификатор {n,}  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
{n,} — повторение n или более раз. Например, a{2,} найдет aa, aaa.
"""
# import re
text = "aaa abc a ab"
matches = re.findall(r"a{2,}", text)
print(matches)

# >>> ['aaa']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  6. Квантификатор {n,m}  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
{n,m} — повторение от n до m раз. Например, a{2,3} найдет aa и aaa.
"""
# import re
text = "aaa abc a ab aag"
matches = re.findall(r"a{2,3}", text)
print(matches)

# >>> ['aaa', 'aa']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  7. Группировка (abc)+  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
Группировка — способ объединения нескольких символов или квантификаторов в единое целое.

(abc)+ — повторение abc один или более раз.
"""
# import re
text = "abcabc ab abcabcabc"
matches = re.findall(r"(abc)+", text)
print(matches)

# >>> ['abc', 'abc']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  8. Группировка (ab|cd)  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
(ab|cd) — ab или cd.
"""
# import re
text = "ab cd abcd"
matches = re.findall(r"(ab|cd)", text)
print(matches)

# >>> ['ab', 'cd', 'ab', 'cd']


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  9. ЗАДАЧА  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
Задача
Напишите программу, которая извлекает информацию о датах и времени из строки.
  - Даты могут быть представлены в формате DD–MM–YYYY или DD/MM/YYYY, а время — в формате HH:MM.
  - Программа должна корректно распознавать эти форматы и выводить найденные даты и время в виде списка кортежей
    (дата, время).
"""
# import re

# Регулярное выражение для поиска дат и времени
pattern = re.compile(r"(\d{2}[-/]\d{2}[-/]\d{4}).*?(\d{2}:\d{2})")


def extract_dates_and_times(text_):  # type: ignore
    # Используем findall для поиска всех совпадений
    mat = pattern.findall(text_)
    return mat


# Пример строки с датами и временем
text = "Встреча запланирована на 23-04-2021 в 14:30 " "и 12/05/2020 в 09:00. Следующее событие " "15-08-2022 в 18:45."

# Извлекаем и выводим даты и время
result = extract_dates_and_times(text)  # type: ignore
print(result)

# >>> [('23-04-2021', '14:30'), ('12/05/2020', '09:00'), ('15-08-2022', '18:45')]


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  10. ЗАДАЧА найти емейл  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
Задача
Найти эмейл
"""
# import re

emails = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

pattern = re.compile(r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

matches = pattern.finditer(emails)  # type: ignore

for match in matches:
    print(match)

# >>> <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
# >>> <re.Match object; span=(25, 53), match='corey.schafer@university.edu'>
# >>> <re.Match object; span=(54, 83), match='corey-321-schafer@my-work.net'>


# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --
print("\n--  --  11. ЗАДАЧА Найти все емейлы @gmail.com  --  --  --\n")
# --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --


"""
Задача
Найти все емейлы @gmail.com
"""
# import re

emails = [
    "user1@gmail.com",
    "user2@yahoo.com",
    "user3@gmail.com",
    "user4@hotmail.com",
]  # type: ignore

# Фильтрация email-адресов, заканчивающихся на @gmail.com
gmail_emails = []
for email in emails:
    if re.search(r"\b\w+@gmail\.com\b", email):
        gmail_emails.append(email)

print(gmail_emails)

# >>> ['user1@gmail.com', 'user3@gmail.com']
