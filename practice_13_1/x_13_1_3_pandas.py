import os

import pandas as pd

"""
Библиотеки pandas основной пакет
poetry add pandas

библиотеку openpyxl для открытия и чтения файлов формата Excel
poetry add openpyxl

Файлы типов структуры библиотеки pandas для статического анализатора mypy
poetry add --group dev pandas-stubs
"""


df = pd.DataFrame({"Yes": [130, 50, 25], "No": [50, 56, 100]})

print(df)


# ---------------------------------------------

print("-- читаем таблицу в файле Excel --")

# Получаем путь к папке, где лежит этот скрипт (data_13_1)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Собираем полный путь к Excel-файлу
file_path = os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx")

# Читаем файл
df = pd.read_excel(file_path)

print(df.shape)
print(df.head())
