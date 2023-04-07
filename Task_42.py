import pandas as pd
r = pd.read_csv('sample_data/california_housing_train.csv')
r.head(10)
r[r['population'] < 50]['households'].max()

# output: 39.0