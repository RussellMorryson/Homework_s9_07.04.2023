"""Задача 40: 
Работать с файлом california_housing_train.csv, который 
находится в папке sample_data. Определить среднюю 
стоимость дома, где кол-во людей от 0 до 500 (population).
"""

import pandas as pd
r = pd.read_csv('sample_data/california_housing_train.csv')
r.head(10)
r[r['population'] < 500]['median_house_value'].mean()

# output: 206683.83635227982