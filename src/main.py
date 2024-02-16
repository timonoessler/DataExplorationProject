import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/apple_quality.csv', sep=',', header=0)
df = df.drop(columns=['A_id'])

print(df.tail())

print(df.dtypes)

df_grouped = df.groupby('Quality').mean()
print(df_grouped)

df.boxplot(column=['Size', 
                   'Weight', 
                   'Sweetness', 
                   'Crunchiness', 
                   'Juiciness', 
                   'Ripeness', 
                   'Acidity'], 
           by='Quality', 
           layout=(1, 7), 
           figsize=(15, 5))

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.5)

plt.suptitle('Boxplot of apple quality attributes')

plt.show()