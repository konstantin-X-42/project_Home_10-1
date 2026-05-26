import os

import pandas as pd

# Получаем путь к папке, где лежит этот скрипт (data_13_1)
current_dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_excel(os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx"))

italy_wine = df.loc[df.country == "Italy"]

print(italy_wine.head())
