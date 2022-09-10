# link https://yulianudelman.medium.com/multi-class-hebrew-text-classification-with-scikit-learn-f8ffaaee013a

import pandas as pd

df = pd.read_csv("fashion_data.csv", index_col=[0], header=[0])
df = df.dropna()
df = df.drop_duplicates()
df = df.reset_index(drop=True)
print(df.info())
print(df.head(5))

