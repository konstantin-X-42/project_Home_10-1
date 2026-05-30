import os

import pandas as pd

# Получаем путь к папке, где лежит этот скрипт (data_13_1)
current_dir = os.path.dirname(os.path.abspath(__file__))
"""
Код фильтрует исходную таблицу, отбирая из неё только строки с итальянскими винами,
выводит первые 5 строк полученного результата
"""
df = pd.read_excel(os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx"))

italy_wine = df.loc[df.country == "Italy"]

print(italy_wine.head())


# ВОЗВРАЩАЕТ
#     Unnamed: 0 country  ...            variety               winery
# 0            0   Italy  ...        White Blend              Nicosia
# 6            6   Italy  ...           Frappato      Terre di Giurfo
# 13          13   Italy  ...  Nerello Mascalese  Masseria Setteporte
# 22          22   Italy  ...        White Blend   Baglio di Pianetto
# 24          24   Italy  ...       Nero d'Avola            Canicattì
#
# [5 rows x 14 columns]
