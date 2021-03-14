import pandas as pd
import os, time

df1 = pd.read_excel("project.xlsx", index_col = 0)
df2 = pd.read_excel("project_2.xlsx", index_col = 0)

df = pd.concat([df1, df2], sort=False) # sort = False 넣어서 공통 컬럼으로 만들기
print(df.head(20))

df.to_excel("project_3.xlsx") 
