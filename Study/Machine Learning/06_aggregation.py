import pandas as pd
import seaborn as sns
import os
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
titanic = sns.load_dataset("titanic")
안녕하세요 액트온입니다.
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
## 그룹 연산 메소드(적용 - 결합 단계)

#클래스 열을 기준으로 분할
grouped = df.groupby(['class'])
std_all = grouped.std()
print(std_all)
#               age       fare  survived
# class
# First   14.802856  78.380373  0.484026
# Second  14.001077  13.417399  0.500623
# Third   12.495398  11.778142  0.428949

std_fare = grouped.fare.std()
print(std_fare)
# class
# First     78.380373
# Second    13.417399
# Third     11.778142

def min_max(x):
    return x.max() - x.min()
# 그룹 객체에 agg() 메소드 적용 - 사용자 정의 함수를 인자로 전달
# 각 그룹의 최대값과 최소값의 차이를 계산하여 그룹별로 집계
agg_minmax = grouped.agg(min_max)
print(agg_minmax)
#           age      fare  survived
# class
# First   79.08  512.3292         1
# Second  69.33   73.5000         1
# Third   73.58   69.5500         1

# 여러 함수를 각 열에 동일하게 적용하여 집계
agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
#          age           sex       fare           survived
#          min   max     min   max  min       max      min max
# class
# First   0.92  80.0  female  male  0.0  512.3292        0   1
# Second  0.67  70.0  female  male  0.0   73.5000        0   1
# Third   0.42  74.0  female  male  0.0   69.5500        0   1

# 각 열마다 다른 함수를 적용하여 집계
agg_sep = grouped.agg({'fare': ['min', 'max'], 'age':'mean'})
print(agg_sep.head())
#        fare                  age
#         min       max       mean
# class
# First   0.0  512.3292  38.233441
# Second  0.0   73.5000  29.877630
# Third   0.0   69.5500  25.140620

# agg_sep.to_excel("agg_sep.xlsx")

# 그룹별 age 열의 평균 집계 연산
age_mean = grouped.age.mean()
print(age_mean)
# First     38.233441
# Second    29.877630
# Third     25.140620
# Name: age, dtype: float64
age_std = grouped.age.std()
print(age_std)
# class
# First     14.802856
# Second    14.001077
# Third     12.495398
# Name: age, dtype: float64

# 그룹 객체의 age 열을 iteration으로 z-score를 계산하여 출력
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key])/age_std.loc[key]
    print("* origin :", key)
    print(group_zscore.head(3))
    print('\n')

# * origin : First
# 1   -0.015770
# 3   -0.218434
# 6    1.065103
# Name: age, dtype: float64

# * origin : Second
# 9    -1.134029
# 15    1.794317
# 17         NaN
# Name: age, dtype: float64

# * origin : Third
# 0   -0.251342
# 2    0.068776
# 4    0.789041
# Name: age, dtype: float64

def z_score(x):
    return (x - x.mean())/ x.std()

# transform 메소드를 이용하여 age열의 데이터를 z-score로 변환
age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]]) # 1, 2, 3 그룹의 첫 데이터 확인
print(age_zscore.loc[0:9])

# 그룹 객체 필터링

# 데이터 개수가 200개 이상인 그룹만을 필터링하여 데이터 프레임으로 반환
grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head())

# age열의 평균이 30보다 작은 그룹만을 필터링하여 데이터 프레임으로 반환
age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter.tail())

# 집계: 각 그룹별 요약 통계 정보 집계
agg_grouped = round(grouped.apply(lambda x: x.describe()), 2)
print(agg_grouped)
#                  age    fare  survived
# class
# First  count  186.00  216.00    216.00
#        mean    38.23   84.15      0.63
#        std     14.80   78.38      0.48
#        min      0.92    0.00      0.00
#        25%     27.00   30.92      0.00
#        50%     37.00   60.29      1.00
#        75%     49.00   93.50      1.00
#        max     80.00  512.33      1.00
# Second count  173.00  184.00    184.00
#        mean    29.88   20.66      0.47
#        std     14.00   13.42      0.50
#        min      0.67    0.00      0.00
#        25%     23.00   13.00      0.00
#        50%     29.00   14.25      0.00
#        75%     36.00   26.00      1.00
#        max     70.00   73.50      1.00
# Third  count  355.00  491.00    491.00
#        mean    25.14   13.68      0.24
#        std     12.50   11.78      0.43
#        min      0.42    0.00      0.00
#        25%     18.00    7.75      0.00
#        50%     24.00    8.05      0.00
#        75%     32.00   15.50      0.00
#        max     74.00   69.55      1.00

age_zscore = grouped.age.apply(z_score)
print(age_zscore.head())
# 0   -0.251342
# 1   -0.015770
# 2    0.068776
# 3   -0.218434
# 4    0.789041

# 필터링 : age열의 데이터 평균이 30보다 작은 그룹만을 필터링하여 출력
age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter)
for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head())

#     age     sex  class     fare  survived
# 0  22.0    male  Third   7.2500         0
# 2  26.0  female  Third   7.9250         1
# 4  35.0    male  Third   8.0500         0
# 5   NaN    male  Third   8.4583         0
# 7   2.0    male  Third  21.0750         0

## 멀티 인덱스

grouped = df.groupby(['class', 'sex'])
gdf = grouped.mean()
print(gdf)
#                      age        fare  survived
# class  sex
# First  female  34.611765  106.125798  0.968085
#        male    41.281386   67.226127  0.368852
# Second female  28.722973   21.970121  0.921053
#        male    30.740707   19.741782  0.157407
# Third  female  21.750000   16.118810  0.500000
#        male    26.507589   12.661633  0.135447

print(gdf.loc['First'])
#               age        fare  survived
# sex
# female  34.611765  106.125798  0.968085
# male    41.281386   67.226127  0.368852

print(gdf.loc[('First', 'female')])
# age          34.611765
# fare        106.125798
# survived      0.968085
# Name: (First, female), dtype: float64

# sex값이 male인 행을 선택하여 출력
print(gdf.xs('male', level='sex'))
#               age       fare  survived
# class
# First   41.281386  67.226127  0.368852
# Second  30.740707  19.741782  0.157407
# Third   26.507589  12.661633  0.135447

## 피벗테이블 만들기

pdf1 = pd.pivot_table(df,
                        index="class",
                        columns="sex",
                        values="age",
                        aggfunc='mean') # 데이터 집계 함수

print(pdf1.head(3))
# ex        female       male
# class
# First   34.611765  41.281386
# Second  28.722973  30.740707
# Third   21.750000  26.507589

# 값에 적용하는 집계 함수 2개 이상 지정 가능하다. - 생존율, 생존자 수 집계
pdf2 = pd.pivot_table(df,
                        index="class",
                        columns="sex",
                        values="survived",
                        aggfunc=['mean', 'sum']) # 데이터 집계 함수

print(pdf2.head(3))
#             mean              sum
# sex       female      male female male
# class
# First   0.968085  0.368852     91   45
# Second  0.921053  0.157407     70   17
# Third   0.500000  0.135447     72   47

# 행, 열 값에 사용할 열을 2개 이상 지정 가능하다. - 평균 나이, 최대 요금 집계
pdf3 = pd.pivot_table(df,
                        index=["class", 'sex'],
                        columns="survived",
                        values=['age', 'fare'],
                        aggfunc=['mean', 'max']) # 데이터 집계 함수

print(pdf3)
#                     mean                                      max
#                      age                   fare               age          fare
# survived               0          1           0           1     0     1       0         1
# class  sex
# First  female  25.666667  34.939024  110.604167  105.978159  50.0  63.0  151.55  512.3292
#        male    44.581967  36.248000   62.894910   74.637320  71.0  80.0  263.00  512.3292
# Second female  36.000000  28.080882   18.250000   22.288989  57.0  55.0   26.00   65.0000
#        male    33.369048  16.022000   19.488965   21.095100  70.0  62.0   73.50   39.0000
# Third  female  23.818182  19.329787   19.773093   12.464526  48.0  63.0   69.55   31.3875
#        male    27.255814  22.274211   12.204469   15.579696  74.0  45.0   69.55   56.4958
print(pdf3.index)
print(pdf3.columns)
# MultiIndex([( 'First', 'female'),
#             ( 'First',   'male'),
#             ('Second', 'female'),
#             ('Second',   'male'),
#             ( 'Third', 'female'),
#             ( 'Third',   'male')],
#            names=['class', 'sex'])
# MultiIndex([('mean',  'age', 0),
#             ('mean',  'age', 1),
#             ('mean', 'fare', 0),
#             ('mean', 'fare', 1),
#             ( 'max',  'age', 0),
#             ( 'max',  'age', 1),
#             ( 'max', 'fare', 0),
#             ( 'max', 'fare', 1)],
#            names=[None, None, 'survived'])


print(pdf3.xs('First'))
#                mean                                      max
#                 age                   fare               age          fare
# survived          0          1           0           1     0     1       0         1
# sex
# female    25.666667  34.939024  110.604167  105.978159  50.0  63.0  151.55  512.3292
# male      44.581967  36.248000   62.894910   74.637320  71.0  80.0  263.00  512.3292
print(pdf3.xs(('First', 'female')))
#             survived
# mean  age   0            25.666667
#             1            34.939024
#       fare  0           110.604167
#             1           105.978159
# max   age   0            50.000000
#             1            63.000000
#       fare  0           151.550000
#             1           512.329200
# Name: (First, female), dtype: float64

print(pdf3.xs('male', level = 'sex')) # 행 인덱스의 sex 레벨이 male인 행을 선택
#                mean                                    max
#                 age                  fare              age          fare
# survived          0          1          0          1     0     1       0         1
# class
# First     44.581967  36.248000  62.894910  74.637320  71.0  80.0  263.00  512.3292
# Second    33.369048  16.022000  19.488965  21.095100  70.0  62.0   73.50   39.0000
# Third     27.255814  22.274211  12.204469  15.579696  74.0  45.0   69.55   56.4958

print(pdf3.xs(('Second', 'male'), level = [0, 'sex'])) # second, male인 행을 선택
#                   mean                               max
#                    age               fare            age        fare
# survived             0       1          0        1     0     1     0     1
# class  sex
# Second male  33.369048  16.022  19.488965  21.0951  70.0  62.0  73.5  39.0

print(pdf3.xs('mean', axis = 1)) # 열 인덱스가 mean인 데이터를 선택
print('\n')
#                      age                   fare
# survived               0          1           0           1
# class  sex
# First  female  25.666667  34.939024  110.604167  105.978159
#        male    44.581967  36.248000   62.894910   74.637320
# Second female  36.000000  28.080882   18.250000   22.288989
#        male    33.369048  16.022000   19.488965   21.095100
# Third  female  23.818182  19.329787   19.773093   12.464526
#        male    27.255814  22.274211   12.204469   15.579696

print(round(pdf3.xs(('mean', 'age'), axis = 1), 2)) # 열 인덱스가 mean, age인 데이터를 선택

# survived           0      1
# class  sex
# First  female  25.67  34.94
#        male    44.58  36.25
# Second female  36.00  28.08
#        male    33.37  16.02
# Third  female  23.82  19.33
#        male    27.26  22.27

print(pdf3.xs(1, level='survived', axis=1)) # 열 인덱스가 mean인 데이터를 선택
print('\n')
#                     mean               max
#                      age        fare   age      fare
# class  sex
# First  female  34.939024  105.978159  63.0  512.3292
#        male    36.248000   74.637320  80.0  512.3292
# Second female  28.080882   22.288989  55.0   65.0000
#        male    16.022000   21.095100  62.0   39.0000
# Third  female  19.329787   12.464526  63.0   31.3875
#        male    22.274211   15.579696  45.0   56.4958

# 레벨 0에서 max값, 레벨 1에서 객실 요금인 fare값, 마지막 레벨 2에서 구조받지 못한 승객 수인 survived=0값을 가져온다.
print(round(pdf3.xs(('max', 'fare', 0), level=[0, 1, 2], axis = 1), 2))
#                   max
#                  fare
# survived            0
# class  sex
# First  female  151.55
#        male    263.00
# Second female   26.00
#        male     73.50
# Third  female   69.55
#        male     69.55
