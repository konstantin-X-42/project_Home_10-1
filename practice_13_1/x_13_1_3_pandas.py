import os

import pandas as pd

"""
Установка библиотеки pandas
poetry add pandas
"""


df = pd.DataFrame({"Yes": [130, 50, 25], "No": [50, 56, 100]})

print(df)


# ---------------------------------------------

# Собираем точный путь к файлу (теперь с расширением .csv)
file_path = os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.csv")

# Загружаем CSV-файл через специальную функцию read_csv
df = pd.read_csv(file_path)
