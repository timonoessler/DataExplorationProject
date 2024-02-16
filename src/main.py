import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/apple_quality.csv', sep=',', header=0)
df = df.drop(columns=['A_id'])

print(df.tail())

print(df.dtypes)

df_grouped = df.groupby('Quality').mean()
print(df_grouped)

