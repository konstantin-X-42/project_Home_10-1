import os

import pandas as pd

# Получаем путь к папке, где лежит этот скрипт (data_13_1)
current_dir = os.path.dirname(os.path.abspath(__file__))

df = pd.read_excel(os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx"))

df.set_index("title", drop=False, inplace=True)

print(df.iloc[0])  # строка №1 по индексу (0)

print(df.loc["Nicosia 2013 Vulkà Bianco  (Etna)"])  # строка №1 по тексту из индекса title
