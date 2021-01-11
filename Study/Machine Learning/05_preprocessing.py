import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset("titanic")
print(df.head())
print(df.info())
# Data columns (total 15 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   survived     891 non-null    int64
#  1   pclass       891 non-null    int64
#  2   sex          891 non-null    object
#  3   age          714 non-null    float64
#  4   sibsp        891 non-null    int64
#  5   parch        891 non-null    int64
#  6   fare         891 non-null    float64
#  7   embarked     889 non-null    object
#  8   class        891 non-null    category
#  9   who          891 non-null    object
#  10  adult_male   891 non-null    bool
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    object
#  13  alive        891 non-null    object
#  14  alone        891 non-null    bool
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)

#열에 있는 값의 개수를 세어보자, (dropna=False)을 통해 NaN값도 같이 세어줄 수 있다.
nan_deck = df['deck'].value_counts(dropna=False)
deck = df['deck'].value_counts()
print(nan_deck)
# NaN    688
# C       59
# B       47
# D       33
# E       32
# A       15
# F       13
# G        4

print(deck)
# C    59
# B    47
# D    33
# E    32
# A    15
# F    13
# G     4

print(df.head().isnull())
#      survived  pclass    sex    age  sibsp  parch   fare  embarked  class    who  adult_male   deck  embark_town  alive  alone      
# 0       False   False  False  False  False  False  False     False  False  False       False   True        False  False  False      
# 1       False   False  False  False  False  False  False     False  False  False       False  False        False  False  False      
# 2       False   False  False  False  False  False  False     False  False  False       False   True        False  False  False      
# 3       False   False  False  False  False  False  False     False  False  False       False  False        False  False  False      
# 4       False   False  False  False  False  False  False     False  False  False       False   True        False  False  False 

print(df.head().isnull().sum(axis=0))
# survived       0
# pclass         0
# sex            0
# age            0
# sibsp          0
# parch          0
# fare           0
# embarked       0
# class          0
# who            0
# adult_male     0
# deck           3
# embark_town    0
# alive          0
# alone          0
# dtype: int64

# axis=0이 열이고 axis=1이 행이다 임마 헷갈리지 말자!
print(df.head().notnull().sum(axis=0))

#열마다 널값을 총 합을 구해보자
print(df.isnull().sum(axis=0))

#누락 데이터 제거하기
df_thresh = df.dropna(axis=1, thresh=500)
# 결측값이 들어있는 행 전체 삭제하기(delete row with NaN) : df.dropna(axis=0)
# 결측값이 들어있는 열 전체 삭제하기 (delete column with NaN) : df.dropna(axis=1)
print(df_thresh.columns)
# Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
#        'embarked', 'class', 'who', 'adult_male', 'embark_town', 'alive',
#        'alone'],
#       dtype='object')
print(df_thresh.info())

#    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male  embark_town alive  alone
# 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  Southampton    no  False
# 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    Cherbourg   yes  False
# 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  Southampton   yes   True
# 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False  Southampton   yes  False
# 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  Southampton    no   True

# subset을 age로 한정하고 nan값이 하나라도 존재하면 삭제하는 how='any'를 적용한다. axis=0로 해당되는 행을 모두 삭제한다.
# how='all'옵션으로 입력하면 모든 데이터가 nan값일 경우에만 삭제가 된다.
df_age = df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))

#비어있는 나이 열에 평균 나이 값을 대신 넣어주기
mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)
print(df.head(10))
#    survived  pclass     sex        age  sibsp  parch     fare embarked   class    who  adult_male deck  embark_town alive  alone
# 0         0       3    male  22.000000      1      0   7.2500        S   Third    man        True  NaN  Southampton    no  False
# 1         1       1  female  38.000000      1      0  71.2833        C   First  woman       False    C    Cherbourg   yes  False
# 2         1       3  female  26.000000      0      0   7.9250        S   Third  woman       False  NaN  Southampton   yes   True
# 3         1       1  female  35.000000      1      0  53.1000        S   First  woman       False    C  Southampton   yes  False
# 4         0       3    male  35.000000      0      0   8.0500        S   Third    man        True  NaN  Southampton    no   True
# 5         0       3    male  29.699118      0      0   8.4583        Q   Third    man        True  NaN   Queenstown    no   True
# 6         0       1    male  54.000000      0      0  51.8625        S   First    man        True    E  Southampton    no   True
# 7         0       3    male   2.000000      3      1  21.0750        S   Third  child       False  NaN  Southampton    no  False
# 8         1       3  female  27.000000      0      2  11.1333        S   Third  woman       False  NaN  Southampton   yes  False
# 9         1       2  female  14.000000      1      0  30.0708        C  Second  child       False  NaN    Cherbourg   yes  False

# embark_town 열의 nan값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
# most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
# df['embark_town'].fillna(most_freq, inplace=True)
# print(df['embark_town'][825:830])
# 825     Queenstown
# 826    Southampton
# 827      Cherbourg
# 828     Queenstown
# 829    Southampton

# 만약 누락 데이터가 nan값이 아닌 다른 값이라면 어떻게 해야할까?
# 넘파이의 np.nan 을 사용해서 nan으로 변환 후 사용하면 된다!
# ex. df.replace('?', np.nan, inplace=True)

# nan값을 이웃하고 있는 값으로 바꾸기
df['embark_town'].fillna(method='ffill', inplace=True)
print(df['embark_town'][825:830])
# 825     Queenstown
# 826    Southampton
# 827      Cherbourg
# 828     Queenstown
# 829     Queenstown

#중복데이터 확인
df = pd.DataFrame({'c1': ['a', 'a', 'b', 'a', 'b'],
                   'c2': [1, 1, 1, 2, 2],
                   'c3': [1, 1, 2, 2, 2]})

# df = pd.DataFrame([['a', 'b', 'c'],
#                    [1, 1, 1],
#                    [1, 1, 2]],
#                    columns=['c1', 'c2', 'c3'])
df_dup = df.duplicated()
print(df_dup) #1행이 중복되었다고 출력됨
# 0    False
# 1     True
# 2    False
# 3    False
# 4    False
# dtype: bool

# 데이터 프레임의 특정 열 데이터에서 중복 값 찾기
col_dup = df['c2'].duplicated()
print(col_dup)
# 0    False
# 1     True
# 2     True
# 3    False
# 4     True

# 데이터 프레임에서 중복 행 제거
df2 = df.drop_duplicates()
print(df2)
#   c1  c2  c3
# 0  a   1   1
# 2  b   1   2
# 3  a   2   2
# 4  b   2   2

# 중복 데이터 제거
df3 = df.drop_duplicates(subset=['c2', 'c3'])
print(df3)
#   c1  c2  c3
# 0  a   1   1
# 2  b   1   2
# 3  a   2   2

## 데이터 표준화
import os
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')

#단위 환산
df = pd.read_csv('auto-mpg.csv', header=None)
df.columns = ["mpg", "cyl", "dis", "hor", "wei", "acc", "model", "origin", "name"]

mpg_to_kpl = 1.60934/3.78541
df['kpl'] = round(df['mpg'] * mpg_to_kpl, 2)
print(df.head())

print(df.dtypes)
# mpg       float64
# cyl         int64
# dis       float64
# hor        object
# wei       float64
# acc       float64
# model       int64
# origin      int64
# name       object
# kpl       float64
# dtype: object

## 자료형 변환하기
# horsepower 열의 고유값 확인 horsepower열은 문자열을 뜻하는 object 자료형이다.
print(df['hor'].unique())
# ['130.0' '165.0' '150.0' '140.0' '198.0' '220.0' '215.0' '225.0' '190.0'
#  '170.0' '160.0' '95.00' '97.00' '85.00' '88.00' '46.00' '87.00' '90.00'
#  '113.0' '200.0' '210.0' '193.0' '?' '100.0' '105.0' '175.0' '153.0'
#  '180.0' '110.0' '72.00' '86.00' '70.00' '76.00' '65.00' '69.00' '60.00'
#  '80.00' '54.00' '208.0' '155.0' '112.0' '92.00' '145.0' '137.0' '158.0'
#  '167.0' '94.00' '107.0' '230.0' '49.00' '75.00' '91.00' '122.0' '67.00'
#  '83.00' '78.00' '52.00' '61.00' '93.00' '148.0' '129.0' '96.00' '71.00'
#  '98.00' '115.0' '53.00' '81.00' '79.00' '120.0' '152.0' '102.0' '108.0'
#  '68.00' '58.00' '149.0' '89.00' '63.00' '48.00' '66.00' '139.0' '103.0'
#  '125.0' '133.0' '138.0' '135.0' '142.0' '77.00' '62.00' '132.0' '84.00'
#  '64.00' '74.00' '116.0' '82.00']
df['hor'].replace('?', np.nan, inplace=True) 
df.dropna(subset=['hor'], axis=0, inplace=True) #누락 데이터 행 삭제
df['hor'] = df['hor'].astype("float") #문자열을 실수형으로 변환
print(df.dtypes)
# mpg       float64
# cyl         int64
# dis       float64
# hor       float64

print(df['hor'][0] * df['hor'][1])


df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)
df['origin'].astype('object')
print(df['origin'].unique())
print(df['origin'].dtype)
# ['USA' 'JPN' 'EU']
# object
# astype("str") == "문자형"
# astype("category") == "범주형"

## 범주형(카테고리) 데이터 처리
#구간 분할(binning) '연속 변수를 일정한 구간으로 나누고 각 구간을 범주형 이산 변수로 변환하는 과정'
# 히스토그램 함수로 3개의 bin으로 나누는 경계값의 리스트 구하기
count, bin_dividers = np.histogram(df['hor'], bins=3)
print(bin_dividers, count)
# [ 46.         107.33333333 168.66666667 230.        ][257 103  32]
# 46~107(1구간), 107~168(2구간), 168~230(3구간)
bin_names = ['저출력', '보통출력', '고출력']

#데이터 구간 분할
df['hp_bin'] = pd.cut(x=df['hor'], # 데이터 배열
                        bins=bin_dividers, # 경계값 리스트
                        labels=bin_names, # bin 이름
                        include_lowest=True) # 첫 경계값 포함

print(df[['hor', 'hp_bin']].head(15))
# 0   130.0   보통출력
# 1   165.0   보통출력
# 2   150.0   보통출력
# 3   150.0   보통출력
# 4   140.0   보통출력
# 5   198.0    고출력
# 6   220.0    고출력
# 7   215.0    고출력
# 8   225.0    고출력
# 9   190.0    고출력
# 10  170.0    고출력
# 11  160.0   보통출력
# 12  150.0   보통출력
# 13  225.0    고출력
# 14   95.0    저출력

# 더미 변수
hor_dummies = pd.get_dummies(df['hp_bin'])
print(hor_dummies.head(5))
# df.to_excel("pp.xlsx")

#sklearn 라이브러리를 이용해서 원핫인코딩을 편하게 처리할 수 있음
#데이터프레임의 'hp_bin'열에 들어있는 범주형 데이터를 0, 1을 원소로 갖는 원핫벡터로 변환함
from sklearn import preprocessing

#전처리를 위한 encoder 객체 만들기
label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

#label인코더로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled))

#2차원 행렬로 형태 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1)
print(onehot_reshaped)
print(type(onehot_reshaped))

#희소행렬로 변환
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))

# [1 1 1 1 1 0 0 0 0 0 0 1 1 0 2]
# <class 'numpy.ndarray'>
# [[1]
#  [1]
#  [1]
#  [1]
#  [1]
#  [0]
#  [0]
#  [0]
#  [0]
#  [0]
#  [0]
#  [1]
#  [1]
#  [0]
#  [2]]
# <class 'numpy.ndarray'>
#   (0, 1)        1.0
#   (1, 1)        1.0
#   (2, 1)        1.0
#   (3, 1)        1.0
#   (4, 1)        1.0
#   (5, 0)        1.0
#   (6, 0)        1.0
#   (7, 0)        1.0
#   (8, 0)        1.0
#   (9, 0)        1.0
#   (10, 0)       1.0
#   (11, 1)       1.0
#   (12, 1)       1.0
#   (13, 0)       1.0
#   (14, 2)       1.0
# <class 'scipy.sparse.csr.csr_matrix'>