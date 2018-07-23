import numpy as np
import pandas as pd
table = [
    ['A', 'Noah', 90],
    ['B', 'Liam', 81],
    ['C', 'William', np.nan],
    ['B', 'Benjamin.', 82],
    ['A', 'Emma.', 90],
    ['C', 'Olivia', np.nan],
    ['A', 'Isabella', 70],
    ['C', 'Amelia', np.nan],
    ['B', 'Mia', 88],
]

df = pd.DataFrame(table,columns = ['class','name','score'])
new_df = df.fillna(df['score'].mean()) 

print(df.groupby(by='class').mean())
print('='*30)
print(df.groupby(by='class').sum())
print('='*30)
print(df.corr())