import os

import pandas as pd

# Получаем путь к папке, где лежит этот скрипт (data_13_1)
current_dir = os.path.dirname(os.path.abspath(__file__))
"""
Читаем таблицу в файле Excel, выводим по индексу и по тексту из индекса
"""
df = pd.read_excel(os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx"))

df.set_index("title", drop=False, inplace=True)

print(df.iloc[0])  # строка №1 по индексу (0)

print("--   --   --  --   --   --  --   --   --  --   --   --  --   --   --")

print(df.loc["Nicosia 2013 Vulkà Bianco  (Etna)"])  # строка №1 по тексту из индекса title

# ВОЗВРАЩАЕТ
# Unnamed: 0                                                               0
# country                                                              Italy
# description              Aromas include tropical fruit, broom, brimston...
# designation                                                   Vulkà Bianco
# points                                                                  87
# price                                                                  NaN
# province                                                 Sicily & Sardinia
# region_1                                                              Etna
# region_2                                                               NaN
# taster_name                                                  Kerin O’Keefe
# taster_twitter_handle                                         @kerinokeefe
# title                                    Nicosia 2013 Vulkà Bianco  (Etna)
# variety                                                        White Blend
# winery                                                             Nicosia
# Name: Nicosia 2013 Vulkà Bianco  (Etna), dtype: object
# --   --   --
# Unnamed: 0                                                               0
# country                                                              Italy
# description              Aromas include tropical fruit, broom, brimston...
# designation                                                   Vulkà Bianco
# points                                                                  87
# price                                                                  NaN
# province                                                 Sicily & Sardinia
# region_1                                                              Etna
# region_2                                                               NaN
# taster_name                                                  Kerin O’Keefe
# taster_twitter_handle                                         @kerinokeefe
# title                                    Nicosia 2013 Vulkà Bianco  (Etna)
# variety                                                        White Blend
# winery                                                             Nicosia
# Name: Nicosia 2013 Vulkà Bianco  (Etna), dtype: object
