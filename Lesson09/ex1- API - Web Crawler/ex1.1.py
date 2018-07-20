#數學分數平均值 - - - (上面填空值時有用到平均值計算方法)
#數學分數總和 - - - (A班平均多少，總分多少，B班平均...)
#數學分數與英文分數的相關係數 - - - ( 可以 google 一下 pandas 算相關係數要用什麼 method。 hint: df.c???() )

import numpy as np
import pandas as pd
# np.nan 是從 numpy 來的，意思是空值，這裡可以先不管他。
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

print(df['score'].isnull()) 

import pandas as pd
import numpy as np
# np.nan 是從 numpy 來的，意思是空值。
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
new_df = df.fillna(df['score'].mean()) # 把空值用平均分數補上
# or new_df = df.fillna({'score': df['score'].mean()}) 也可以傳入字典來選擇 哪些欄位 要用 什麼資料 填補空值

print(new_df)

print(df.groupby(by='class').sum())
print(df.groupby(by='class').mean())
print(df.corr())