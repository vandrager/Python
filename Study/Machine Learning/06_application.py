import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic")

df = titanic.loc[:, ['age', 'fare']]
print(df.info())
df['ten'] = 10


def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b
a = add_10(10)
b = add_two_obj(10, 20)
print(a, b)

#시리즈의 원소에 apply() 적용


df['age'].fillna(df['age'].mean(), inplace = True)
print(df.info())

# 시리즈 객체에 적용
sr1 = df['age'].apply(add_10) # n = df['age']의 모든 원소
print(sr1)

# 시리즈 객체와 숫자에 적용: 2개의 인수(시리즈 + 숫자)
sr2 = df['age'].apply(add_two_obj, b = 10) # a = df['age']의 모든 원소 b = 10
print(sr2)

# lambda 함수 활용: 시리즈 객체에 적용
sr3 = df['age'].apply(lambda x: add_10(x)) # x = df['age']
print(sr3)

# 데이터 프레임 원소에 함수 매핑
# 데이터 프레임 원소에 applymap() 적용

df_map = df.applymap(add_10)
print(df_map.head())
#     age     fare  ten
# 0  32.0  17.2500   20
# 1  48.0  81.2833   20
# 2  36.0  17.9250   20
# 3  45.0  63.1000   20
# 4  45.0  18.0500   20

## 시리즈 객체에 함수 매핑
# 데이터프레임의 각 열에 함수 매핑
def missing_value(series): # 시리즈를 인자로 전달
    return series.isnull() # 불린 시리즈를 반환

result = df.apply(missing_value, axis=0)
print(result.tail(10))


def min_max(x):
    return x.max() - x.min()

result2 = df.apply(min_max)
print(result2)
# age      79.5800
# fare    512.3292
# ten       0.0000
# dtype: float64

# 데이터프레임의 각 행에 함수 매핑

df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)
print(df.head(3))
#     age     fare  ten   add
# 0  22.0   7.2500   10  32.0
# 1  38.0  71.2833   10  48.0
# 2  26.0   7.9250   10  36.0

# 데이터 프레임 객체에 함수 매핑
# 데이터 프레임 객체를 함수에 매핑하려면 pipe() 메소드를 활용한다.
def missing_count(x):
    return missing_value(x).sum()

def total_number_missing(x):
    return missing_count(x).sum()
df = titanic.loc[:, ['age', 'fare']]
result_df = df.pipe(missing_value)
print(result_df.head(4))

result_series = df.pipe(missing_count)
print(result_series)
# age     177
# fare      0
result_total = df.pipe(total_number_missing)
print(result_total)
# 177

## 열 재구성
df = titanic.loc[0:4, 'survived':'age']
print(df, '\n')
#    survived  pclass     sex   age
# 0         0       3    male  22.0
# 1         1       1  female  38.0
# 2         1       3  female  26.0
# 3         1       1  female  35.0
# 4         0       3    male  35.0 

columns = list(df.columns.values)
print(columns)
# ['survived', 'pclass', 'sex', 'age']

column_sorted = sorted(columns)
df_sorted = df[column_sorted]
print(df_sorted)
#     age  pclass     sex  survived
# 0  22.0       3    male         0
# 1  38.0       1  female         1
# 2  26.0       3  female         1
# 3  35.0       1  female         1
# 4  35.0       3    male         0

columns_reversed = list(reversed(columns))
df_reversed = df[columns_reversed]
print(df_reversed)
#     age     sex  pclass  survived
# 0  22.0    male       3         0
# 1  38.0  female       1         1
# 2  26.0  female       3         1
# 3  35.0  female       1         1
# 4  35.0    male       3         0

column_custom = ['pclass', 'sex', 'age', 'survived']
df_custom = df[column_custom]
print(df_custom)
#    pclass     sex   age  survived
# 0       3    male  22.0         0
# 1       1  female  38.0         1
# 2       3  female  26.0         1
# 3       1  female  35.0         1
# 4       3    male  35.0         0
import os
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
df = pd.read_excel("주가데이터.xlsx")
print(df.head(3))
print(df.dtypes)
# 연월일     datetime64[ns]
# 당일종가             int64
# 전일종가             int64
# 시가               int64
# 고가               int64
# 저가               int64
# 거래량              int64

df['연월일'] = df['연월일'].astype('str') # 문자열 메소드 사용을 위해 자료형 변경
dates = df['연월일'].str.split('-') # 문자열을 split 메소드로 분리
# print(dates.head())
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)

df.drop('연월일', axis=1, inplace=True)
print(df.columns)
# ['당일종가', '전일종가', '시가', '고가', '저가', '거래량', '연', '월', '일']
change = ['연', '월', '일', '당일종가', '전일종가', '시가', '고가', '저가', '거래량']
df = df[change]
print(df.head(5))

## 필터링
titanic = sns.load_dataset("titanic")
mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())
#     survived  pclass     sex   age  sibsp  parch      fare embarked   class    who  adult_male deck  embark_town alive  alone
# 9          1       2  female  14.0      1      0   30.0708        C  Second  child       False  NaN    Cherbourg   yes  False
# 14         0       3  female  14.0      0      0    7.8542        S   Third  child       False  NaN  Southampton    no   True
# 22         1       3  female  15.0      0      0    8.0292        Q   Third  child       False  NaN   Queenstown   yes   True
# 27         0       1    male  19.0      3      2  263.0000        S   First    man        True    C  Southampton    no  False
# 38         0       3  female  18.0      2      0   18.0000        S   Third  woman       False  NaN  Southampton    no  False

mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_fe_un10 = titanic.loc[mask2, :]
print(df_fe_un10.head())
#      survived  pclass     sex   age  sibsp  parch      fare embarked   class    who  adult_male deck  embark_town alive  alone
# 10          1       3  female  4.00      1      1   16.7000        S   Third  child       False    G  Southampton   yes  False
# 24          0       3  female  8.00      3      1   21.0750        S   Third  child       False  NaN  Southampton    no  False
# 43          1       2  female  3.00      1      2   41.5792        C  Second  child       False  NaN    Cherbourg   yes  False
# 58          1       2  female  5.00      1      2   27.7500        S  Second  child       False  NaN  Southampton   yes  False
# 119         0       3  female  2.00      4      2   31.2750        S   Third  child       False  NaN  Southampton    no  False

mask3 = (titanic.age < 10) | (titanic.sex == 'female') | (titanic.age > 65)
df_m3 = titanic.loc[mask3, ['age', 'sex', 'alone']]
print(df_m3.head())
#     age     sex  alone
# 1  38.0  female  False
# 2  26.0  female   True
# 3  35.0  female  False
# 7   2.0    male  False
# 8  27.0  female  False

## isin 메소드 활용

# ipython 디스플레이 설정 변경 - 출력할 최대 열의 개수
pd.set_option('display.max_columns', 10) # 출력할 열의 개수 한도
# 함께 탑승한 형제 또는 배우자의 수가 3, 4, 5,인 승객만 따로 출력
mask3 = titanic['sibsp'] == 3 
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5
df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head())
#     survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town  \
# 7          0       3    male   2.0      3  ...       False   NaN  Southampton
# 16         0       3    male   2.0      4  ...       False   NaN   Queenstown
# 24         0       3  female   8.0      3  ...       False   NaN  Southampton
# 27         0       1    male  19.0      3  ...        True     C  Southampton
# 50         0       3    male   7.0      4  ...       False   NaN  Southampton

#    alive  alone
# 7     no  False
# 16    no  False
# 24    no  False
# 27    no  False
# 50    no  False

isin_filter =titanic['sibsp'].isin([3, 4, 5])
df_isin = titanic[isin_filter]
print(df_isin.head())
#     survived  pclass     sex   age  sibsp  ...  adult_male  deck  embark_town  \
# 7          0       3    male   2.0      3  ...       False   NaN  Southampton
# 16         0       3    male   2.0      4  ...       False   NaN   Queenstown
# 24         0       3  female   8.0      3  ...       False   NaN  Southampton
# 27         0       1    male  19.0      3  ...        True     C  Southampton
# 50         0       3    male   7.0      4  ...       False   NaN  Southampton

#    alive  alone
# 7     no  False
# 16    no  False
# 24    no  False
# 27    no  False
# 50    no  False

## 데이터 프레임 합치기

# 데이터 프레임 연결

df1 = pd.DataFrame([[1, 2, 3],
                    [2, 3, 4],
                    [3, 4, 5],
                    [6, 7, 9]],
                    index=[0, 1, 2, 3],
                    columns=['a', 'b', 'c'])

df2 = pd.DataFrame([[1, 2, 3],
                    [2, 3, 4],
                    [3, 4, 5],
                    [6, 7, 9]],
                    index=[2, 3, 4, 5],
                    columns=['b', 'c', 'd'])

result = pd.concat([df1, df2]) # concat으로 이어붙이기, 열이름은 join=outer 합집합 옵션이 기본 적용/ join=inner 옵션의 경우 공통으로 속하는 교집합이 기준이 됨
print(result)
#      a  b  c    d
# 0  1.0  2  3  NaN
# 1  2.0  3  4  NaN
# 2  3.0  4  5  NaN
# 3  6.0  7  9  NaN
# 2  NaN  1  2  3.0
# 3  NaN  2  3  4.0
# 4  NaN  3  4  5.0
# 5  NaN  6  7  9.0

result2 = pd.concat([df1, df2], join='inner')
print(result2)
#    b  c
# 0  2  3
# 1  3  4
# 2  4  5
# 3  7  9
# 2  1  2
# 3  2  3
# 4  3  4
# 5  6  7

result3 = pd.concat([df1, df2], ignore_index=True) # 기존 행 인덱스를 무시하고 새로운 행 인덱스를 설정하기
print(result3)
#      a  b  c    d
# 0  1.0  2  3  NaN
# 1  2.0  3  4  NaN
# 2  3.0  4  5  NaN
# 3  6.0  7  9  NaN
# 4  NaN  1  2  3.0
# 5  NaN  2  3  4.0
# 6  NaN  3  4  5.0
# 7  NaN  6  7  9.0

result4= pd.concat([df1, df2], axis=1)
print(result4)
#      a    b    c    b    c    d
# 0  1.0  2.0  3.0  NaN  NaN  NaN
# 1  2.0  3.0  4.0  NaN  NaN  NaN
# 2  3.0  4.0  5.0  1.0  2.0  3.0
# 3  6.0  7.0  9.0  2.0  3.0  4.0
# 4  NaN  NaN  NaN  3.0  4.0  5.0
# 5  NaN  NaN  NaN  6.0  7.0  9.0

sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')

result5 = pd.concat([df1, sr1], axis=1)
print(result5)
#    a  b  c   e
# 0  1  2  3  e0
# 1  2  3  4  e1
# 2  3  4  5  e2
# 3  6  7  9  e3

result6 = pd.concat([df2, sr2], axis=1, sort=True)
print(result6)
#    b  c  d    f
# 2  1  2  3  NaN
# 3  2  3  4   f0
# 4  3  4  5   f1
# 5  6  7  9   f2

result7 = pd.concat([sr1, sr3], axis=1)
print(result7)
#     e   g
# 0  e0  g0
# 1  e1  g1
# 2  e2  g2
# 3  e3  g3
result8 = pd.concat([sr1, sr3], axis=0)
print(result8)
# 0    e0
# 1    e1
# 2    e2
# 3    e3
# 0    g0
# 1    g1
# 2    g2
# 3    g3

# 데이터 프레임 병합
pd.set_option('display.max.colwidth', 20) # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True) #유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터 프레임 만들기
df1 = pd.read_excel("stock price.xlsx")
df2 = pd.read_excel("stock valuation.xlsx")

merge_inner = pd.merge(df1, df2) # 합치기 교집합
print(merge_inner)

merge_outer = pd.merge(df1, df2, how="outer", on="id") # id기준으로 합치기 합집합
print(merge_outer)

# 왼쪽 데이터 프레임 기준, 키 값 분리(id_x, id_y로 나뉘게 된다.)
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on="name")
print(merge_left)
#   id_x    stock_name          value   price      id_y          name  \
# 0  128940      한미약품   59385.666667  421000       NaN           NaN
# 1  130960        CJ E&M   58540.666667   98900  130960.0        CJ E&M
# 2  138250    엔에스쇼핑   14558.666667   13200       NaN           NaN
# 3  139480        이마트  239230.833333  254500  139480.0        이마트
# 4  142280  녹십자엠에스     468.833333   10200       NaN           NaN

# 오른쪽 데이터 프레임 기준, 키 값 분리
merge_right = pd.merge(df1, df2, how="right", left_on='stock_name', right_on="name")
print(merge_right)
#        id_x    stock_name          value     price    id_y              name  \
# 0  130960.0        CJ E&M   58540.666667   98900.0  130960            CJ E&M
# 1       NaN           NaN            NaN       NaN  136480              하림
# 2       NaN           NaN            NaN       NaN  138040    메리츠금융지주
# 3  139480.0        이마트  239230.833333  254500.0  139480            이마트
# 4  145990.0        삼양사   82750.000000   82000.0  145990            삼양사

# 불린 인덱싱과 결합하여 원하는 데이터 찾기
price = df1[df1['price'] < 50000]
print(price.head())
#        id    stock_name         value  price
# 2  138250    엔에스쇼핑  14558.666667  13200
# 4  142280  녹십자엠에스    468.833333  10200
# 9  204210  모두투어리츠   3093.333333   3475

value = pd.merge(price, df2)
print(value)
#        id    stock_name        value  price          name        eps   bps  \
# 0  204210  모두투어리츠  3093.333333   3475  모두투어리츠  85.166667  5335

#          per       pbr
# 0  40.802348  0.651359

# 주식 데이터를 가져와서 데이터 프레임 만들기
df1 = pd.read_excel("stock price.xlsx", index_col='id')
df2 = pd.read_excel("stock valuation.xlsx", index_col='id')

df3 = df1.join(df2) # join 함수는 merge와는 다르게 기본적으로 행을 기준으로 결합한다.
print(df3.head())

df4 = df1.join(df2, how="inner") # 합쳐서 교집합 구하기
print(df4.head())
#           stock_name          value   price          name           eps  \
# id
# 130960        CJ E&M   58540.666667   98900        CJ E&M   6301.333333
# 139480        이마트  239230.833333  254500        이마트  18268.166667
# 145990        삼양사   82750.000000   82000        삼양사   5741.000000
# 185750        종근당   40293.666667  100500        종근당   3990.333333
# 204210  모두투어리츠    3093.333333    3475  모두투어리츠     85.166667

#            bps        per       pbr
# id
# 130960   54068  15.695091  1.829178
# 139480  295780  13.931338  0.860437
# 145990  108090  14.283226  0.758627
# 185750   40684  25.185866  2.470259
# 204210    5335  40.802348  0.651359

## 그룹 연산
## 1단계) 분할, 2단계) 적용, 3단계) 결합
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class'])
print(df.head())
print(grouped)
#     age     sex  class     fare  survived
# 0  22.0    male  Third   7.2500         0
# 1  38.0  female  First  71.2833         1
# 2  26.0  female  Third   7.9250         1
# 3  35.0  female  First  53.1000         1
# 4  35.0    male  Third   8.0500         0
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000001D778A6E6D0>

for key, group in grouped:
    print("* key :", key)
    print("* number :", len(group))
    print(group.head())
    print('\n')

# * key : First
# * number : 216
#      age     sex  class     fare  survived
# 1   38.0  female  First  71.2833         1
# 3   35.0  female  First  53.1000         1
# 6   54.0    male  First  51.8625         0
# 11  58.0  female  First  26.5500         1
# 23  28.0    male  First  35.5000         1


# * key : Second
# * number : 184
#      age     sex   class     fare  survived
# 9   14.0  female  Second  30.0708         1
# 15  55.0  female  Second  16.0000         1
# 17   NaN    male  Second  13.0000         1
# 20  35.0    male  Second  26.0000         0
# 21  34.0    male  Second  13.0000         1


# * key : Third
# * number : 491
#     age     sex  class     fare  survived
# 0  22.0    male  Third   7.2500         0
# 2  26.0  female  Third   7.9250         1
# 4  35.0    male  Third   8.0500         0
# 5   NaN    male  Third   8.4583         0
# 7   2.0    male  Third  21.0750         0

average = grouped.mean()
print(average)
#               age       fare  survived
# class
# First   38.233441  84.154687  0.629630
# Second  29.877630  20.662183  0.472826
# Third   25.140620  13.675550  0.242363

# 개별 그룹 선택하기
group3 = grouped.get_group('Third')
print(group3.head(3))
#    age     sex  class   fare  survived
# 0  22.0    male  Third  7.250         0
# 2  26.0  female  Third  7.925         1
# 4  35.0    male  Third  8.050         0

# 여러 열을 기준을 그룹화하기
grouped_2 = df.groupby(['class', 'sex'])

for key, group in grouped_2:
    print("* key :", key)
    print("* number :", len(group))
    print(group.head())
    print('\n')
# * key : ('Third', 'female')
# * number : 144
#      age     sex  class     fare  survived
# 2   26.0  female  Third   7.9250         1
# 8   27.0  female  Third  11.1333         1
# 10   4.0  female  Third  16.7000         1
# 14  14.0  female  Third   7.8542         0
# 18  31.0  female  Third  18.0000         0


# * key : ('Third', 'male')
# * number : 347
#      age   sex  class     fare  survived
# 0   22.0  male  Third   7.2500         0
# 4   35.0  male  Third   8.0500         0
# 5    NaN  male  Third   8.4583         0
# 7    2.0  male  Third  21.0750         0
# 12  20.0  male  Third   8.0500         0

average_2 = round(grouped_2.mean(), 2)
print(average_2)
#                 age    fare  survived
# class  sex
# First  female  34.61  106.13      0.97
#        male    41.28   67.23      0.37
# Second female  28.72   21.97      0.92
#        male    30.74   19.74      0.16
# Third  female  21.75   16.12      0.50
#        male    26.51   12.66      0.14

group3f = grouped_2.get_group(('Third', 'female'))
print(group3f)
#       age     sex  class     fare  survived
# 2    26.0  female  Third   7.9250         1
# 8    27.0  female  Third  11.1333         1
# 10    4.0  female  Third  16.7000         1
# 14   14.0  female  Third   7.8542         0
# 18   31.0  female  Third  18.0000         0

