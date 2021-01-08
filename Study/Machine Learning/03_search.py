import os, re, requests
import pandas as pd
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")

car = pd.read_csv("auto-mpg.csv", header=None)
car.columns = ["mpg", "cyl", "dis", "hor", "wei", "acc", "model", "origin", "name"]
print(car.head(5))
print(car.shape) #모양 확인하기(행, 열)
print(car.info()) #데이터 프레임의 기본 정보
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 397 entries, 0 to 396
# Data columns (total 9 columns):
#  #   Column                     Non-Null Count  Dtype
# ---  ------                     --------------  -----
#  0   18.0                       397 non-null    float64
#  1   8                          397 non-null    int64
#  2   307.0                      397 non-null    float64
#  3   130.0                      397 non-null    object
#  4   3504.                      397 non-null    float64
#  5   12.0                       397 non-null    float64
#  6   70                         397 non-null    int64
#  7   1                          397 non-null    int64
#  8   chevrolet chevelle malibu  397 non-null    object
# dtypes: float64(4), int64(3), object(2)
# memory usage: 28.0+ KB
# None

print(car.dtypes) #자료형 확인
# 18.0                         float64
# 8                              int64
# 307.0                        float64
# 130.0                         object
# 3504.                        float64
# 12.0                         float64
# 70                             int64
# 1                              int64
# chevrolet chevelle malibu     object
print(car.describe()) #기초통계량 확인
#              18.0           8       307.0        3504.        12.0          70           1
# count  397.000000  397.000000  397.000000   397.000000  397.000000  397.000000  397.000000
# mean    23.528463    5.448363  193.139798  2969.080605   15.577078   76.025189    1.574307
# std      7.820926    1.698329  104.244898   847.485218    2.755326    3.689922    0.802549
# min      9.000000    3.000000   68.000000  1613.000000    8.000000   70.000000    1.000000
# 25%     17.500000    4.000000  104.000000  2223.000000   13.900000   73.000000    1.000000
# 50%     23.000000    4.000000  146.000000  2800.000000   15.500000   76.000000    1.000000
# 75%     29.000000    8.000000  262.000000  3609.000000   17.200000   79.000000    2.000000
# max     46.600000    8.000000  455.000000  5140.000000   24.800000   82.000000    3.000000

print(car.count())
# mpg       398
# cyl       398
# dis       398
# hor       398
# wei       398
# acc       398
# model     398
# origin    398
# name      398
# dtype: int64
print(car["model"].value_counts())
# 73    40
# 78    36
# 76    34
# 82    31
# 75    30
# 81    29
# 80    29
# 79    29
# 70    29
# 77    28
# 72    28
# 71    28
# 74    27
# Name: model, dtype: int64

print(car[["model", "acc"]].mean())
print(car[["model", "acc"]].median())
print(car[["model", "acc"]].max())
print(car[["model", "acc"]].min())
print(car[["model", "acc"]].sum())
print(car[["model", "acc"]].std())
print(car[["model", "acc"]].var())
print(car[["model", "acc"]].corr())

df = pd.read_excel("남북한발전전력량.xlsx")
df_ns = df.iloc[[0, 5], 2:]
df_ns.index = ['south', 'north']
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head())

print(df_ns['1990': ])
print(df_ns.iloc[0:])
