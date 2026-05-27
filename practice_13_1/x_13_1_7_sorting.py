import os

import pandas as pd

# Получаем путь к папке, где лежит этот скрипт (data_13_1)
current_dir = os.path.dirname(os.path.abspath(__file__))
"""
группировка данных о вине по странам, вычисляет среднюю стоимость бутылки для каждой страны
"""
df = pd.read_excel(os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx"))

country_df = df.groupby("country")

print(country_df.price.mean())

# ВОЗВРАЩАЕТ
# country
# Argentina                 24.510117
# Armenia                   14.500000
# Australia                 35.437663
# Austria                   30.762772
# Bosnia and Herzegovina    12.500000
# Brazil                    23.765957
# Bulgaria                  14.645390
# Canada                    35.712598
# Chile                     20.786458
# China                     18.000000
# Croatia                   25.450704
# Cyprus                    16.272727
# Czech Republic            24.250000
# Egypt                           NaN
# England                   51.681159
# France                    41.139120
# Georgia                   19.321429
# Germany                   42.257547
# Greece                    22.364425
# Hungary                   40.648276
# India                     13.333333
# Israel                    31.768916
# Italy                     39.663770
# Lebanon                   30.685714
# Luxembourg                23.333333
# Macedonia                 15.583333
# Mexico                    26.785714
# Moldova                   16.745763
# Morocco                   19.500000
# New Zealand               26.931785
# Peru                      18.062500
# Portugal                  26.218256
# Romania                   15.241667
# Serbia                    24.500000
# Slovakia                  16.000000
# Slovenia                  24.812500
# South Africa              24.668987
# Spain                     28.215275
# Switzerland               85.285714
# Turkey                    24.633333
# US                        36.573464
# Ukraine                    9.214286
# Uruguay                   26.403670
# Name: price, dtype: float64

# ----------------------------------------------------------------------
print("--   --   --  --   --   --  --   --   --  --   --   --  --   --   --")

# import os
# import pandas as pd

# 1. Автоматически определяем путь к папке со скриптом
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Собираем точный путь к Excel-файлу внутри папки data_13_1
file_path = os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx")

# 3. Читаем Excel-файл
df = pd.read_excel(file_path)
"""
код загружает таблицу с данными о винах из Excel-файла, находит самые дорогие и выводит их цены на экран
"""
# 4. Сортируем по цене
df.sort_values(by="price", inplace=True, ascending=False)

# 5. Выводим результат
print(df.head().price)

# ВОЗВРАЩАЕТ
# 80290     3300.0
# 98380     2500.0
# 15840     2500.0
# 120391    2013.0
# 65352     2000.0
# Name: price, dtype: float64

# ----------------------------------------------------------------------
print("--   --   --  --   --   --  --   --   --  --   --   --  --   --   --")

# import os
# import pandas as pd

# Получаем путь к папке, где лежит этот скрипт (data_13_1)
current_dir = os.path.dirname(os.path.abspath(__file__))
"""
код группирует данные по странам и рассчитывает для каждой из них средние показатели цены и рейтинга
"""
df = pd.read_excel(os.path.join(current_dir, "data_13_1", "winemag-data-130k-v2.xlsx"))

new_df = df.groupby("country").agg({"price": "mean", "points": "mean"})

print(new_df.head())

# ВОЗВРАЩАЕТ
#                             price     points
# country
# Argentina               24.510117  86.710263
# Armenia                 14.500000  87.500000
# Australia               35.437663  88.580507
# Austria                 30.762772  90.101345
# Bosnia and Herzegovina  12.500000  86.500000
