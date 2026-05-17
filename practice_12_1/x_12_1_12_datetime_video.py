"""
Задача
1. Получить текущую дату и время.
2. Получить год, месяц, день, час, минуту и секунду из объекта.
3. Преобразовать объект даты и времени в строку.(Перевод раскладки: «d ntrcn» — это «в текст»).
"""

import datetime

date_obj = datetime.datetime.now()

print(date_obj.year)  # >>> 2026
print(date_obj.month)  # >>> 5
print(date_obj.day)  # >>> 17
print(date_obj.hour)  # >>> 22
print(date_obj.minute)  # >>> 10
print(date_obj.second)  # >>> 9

date_str = date_obj.strftime("%d-%m-%Y %H:%M:%S")

print(date_str)  # >>> 17-05-2026 22:13:08
