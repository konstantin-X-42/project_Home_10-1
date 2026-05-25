import csv

print("\n--- Читаем файл-CSV функцией reader, выводит список построчно ---\n")

with open("data_13_1/students.csv") as st_file:  # если файл в корне проекта прописывается: 'students.csv'
    reader = csv.reader(st_file)  # создает объект-читатель (итератор), выдаёт построчно
    next(reader)  # первая строка (заголовок) забираем из конвейера, на выходе будет отсутствовать
    for row in reader:  # построчно выдает в цикле
        if float(row[2]) > 4.5:  # обращаемся по индексу и выводим бал более 4.5
            print(row)

# ['Alice', '20', '4.7']
# ['Charlie', '22', '4.8']

# ----------------------------------------------------------------------

print("\n--- Читаем файл-CSV функцией DictReader, выводит словарь построчно ---\n")


with open("data_13_1/students.csv") as st_file:
    reader_2 = csv.DictReader(st_file)
    for row_2 in reader_2:
        # print(row_2) # Читаем файл-CSV функцией DictReader, выводим всё содержимое файла
        if float(row_2["avg_grade"]) > 4.5:  # обращаемся по ключу
            print(row_2)

# {'name': 'Alice', 'age': '20', 'avg_grade': '4.7'}
# {'name': 'Charlie', 'age': '22', 'avg_grade': '4.8'}
