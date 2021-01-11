import pandas as pd
import numpy as np
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")

df = pd.read_csv("auto-mpg.csv", header=None)
df.columns = ["mpg", "cyl", "dis", "hor", "wei", "acc", "model", "origin", "name"]
df['hor'].replace('?', np.nan, inplace=True) 
df.dropna(subset=['hor'], axis=0, inplace=True)
df['hor'] = df['hor'].astype("float")

print(df['hor'].describe())
# count    392.000000
# mean     104.469388
# std       38.491160
# min       46.000000
# 25%       75.000000
# 50%       93.500000
# 75%      126.000000
# max      230.000000
# Name: hor, dtype: float64

#horespower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
df.hor = df.hor/abs(df.hor.max())
print(df.hor.head(10))
print(df.head(5))
# 0    0.565217
# 1    0.717391
# 2    0.652174
# 3    0.652174
# 4    0.608696
# 5    0.860870
# 6    0.956522
# 7    0.934783
# 8    0.978261
# 9    0.826087
# Name: hor, dtype: float64
min_x = df.hor - df.hor.min()
min_max = df.hor.max() - df.hor.min()
df.hor = min_x/min_max
print(df.hor.head(10))
print(df.hor.describe())
# 0    0.456522
# 1    0.646739
# 2    0.565217
# 3    0.565217
# 4    0.510870
# 5    0.826087
# 6    0.945652
# 7    0.918478
# 8    0.972826
# 9    0.782609
# Name: hor, dtype: float64
# count    392.000000
# mean       0.317768
# std        0.209191
# min        0.000000
# 25%        0.157609
# 50%        0.258152
# 75%        0.434783
# max        1.000000


## 시계열 데이터
# 판다스의 시간 표시 방식 중에서 시계열 데이터 표현에 자주 이용되는 두 가지 유형이 있다.
# 특정한 시점을 기록하는 timestamp와 두 시점 사이의 일정한 기간을 나타내는 period가 있다.

df = pd.read_csv("stock-data.csv")
print(df.head())
#          Date  Close  Start   High    Low  Volume
# 0  2018-07-02  10100  10850  10900  10000  137977
# 1  2018-06-29  10700  10550  10900   9990  170253
# 2  2018-06-28  10400  10900  10950  10150  155769
# 3  2018-06-27  10900  10800  11050  10500  133548
# 4  2018-06-26  10800  10900  11000  10700   63039
print(df.info())
print(df.describe()) 
#문자열 데이터(시리즈 객체)를 판다스 타임스태프로 변환
df['new_Date'] = pd.to_datetime(df['Date']) #df에 새로운 열로 추가
print(df.head())
print(type(df['new_Date'])) # <class 'pandas.core.series.Series'>

#timestamp를 period로 변환
dates = ['2019-01-01', '2020-03-20', '2021-03-28'] 
ts_dates = pd.to_datetime(dates) #timestamp 생성
pr_day = ts_dates.to_period(freq="D")
print(pr_day)
pr_month = ts_dates.to_period(freq="M")
print(pr_month)
pr_year = ts_dates.to_period(freq="A")
print(pr_year)
# PeriodIndex(['2019-01-01', '2020-03-20', '2021-03-28'], dtype='period[D]', freq='D')
# PeriodIndex(['2019-01', '2020-03', '2021-03'], dtype='period[M]', freq='M')
# PeriodIndex(['2019', '2020', '2021'], dtype='period[A-DEC]', freq='A-DEC')
# freq에 대한 더 자세한 내용은 --> https://pandas.pydata.org/docs/user_guide/timeseries.html

# 시계열 데이터 만들기
# Timestamp 배열
ts_ms = pd.date_range(start='2019-01-01', #날짜 범위 시작
                        end=None, #날짜 범위 끝
                        periods=6, # 생성할 타임스태프 개수
                        freq='MS', # 시간 간격(MS: 월의 시작일)
                        tz='Asia/Seoul')

print(ts_ms)
# DatetimeIndex(['2019-01-01 00:00:00+09:00', '2019-02-01 00:00:00+09:00',
#                '2019-03-01 00:00:00+09:00', '2019-04-01 00:00:00+09:00',
#                '2019-05-01 00:00:00+09:00', '2019-06-01 00:00:00+09:00'],
#               dtype='datetime64[ns, Asia/Seoul]', freq='MS')

ts_me = pd.date_range(start='2019-01-01', #날짜 범위 시작
                        periods=6, # 생성할 타임스태프 개수
                        freq='M', # 시간 간격(MS: 월의 시작일)
                        tz='Asia/Seoul')

print(ts_me)
# DatetimeIndex(['2019-01-31 00:00:00+09:00', '2019-02-28 00:00:00+09:00',
#                '2019-03-31 00:00:00+09:00', '2019-04-30 00:00:00+09:00',
#                '2019-05-31 00:00:00+09:00', '2019-06-30 00:00:00+09:00'],
#               dtype='datetime64[ns, Asia/Seoul]', freq='M')

ts_3m = pd.date_range(start='2019-01-01', #날짜 범위 시작
                        periods=6, # 생성할 타임스태프 개수
                        freq='3M', # 시간 간격(MS: 월의 시작일)
                        tz='Asia/Seoul')

print(ts_3m)
# DatetimeIndex(['2019-01-31 00:00:00+09:00', '2019-04-30 00:00:00+09:00',
#                '2019-07-31 00:00:00+09:00', '2019-10-31 00:00:00+09:00',
#                '2020-01-31 00:00:00+09:00', '2020-04-30 00:00:00+09:00'],
#               dtype='datetime64[ns, Asia/Seoul]', freq='3M')

# Period 배열
pr_m = pd.period_range(start='2019-01-01', #날짜 범위 시작
                        end=None,
                        periods=3, # 생성할 타임스태프 개수
                        freq='M') # 시간 간격(MS: 월의 시작일)

print(pr_m)

pr_H = pd.period_range(start='2019-01-01', #날짜 범위 시작
                        end=None,
                        periods=3, # 생성할 타임스태프 개수
                        freq='H') # 시간 간격(MS: 월의 시작일)

print(pr_H)

pr_2H = pd.period_range(start='2019-01-01', #날짜 범위 시작
                        end=None,
                        periods=3, # 생성할 타임스태프 개수
                        freq='2H') # 시간 간격(MS: 월의 시작일)

print(pr_2H)
print(pr_2H[0])
# PeriodIndex(['2019-01', '2019-02', '2019-03'], dtype='period[M]', freq='M')
# PeriodIndex(['2019-01-01 00:00', '2019-01-01 01:00', '2019-01-01 02:00'], dtype='period[H]', freq='H')
# PeriodIndex(['2019-01-01 00:00', '2019-01-01 02:00', '2019-01-01 04:00'], dtype='period[2H]', freq='2H')
# 2019-01-01 00:00

# 시계열 데이터 활용하기
# dt 속성을 이용하여 new date 열의 연월일 정보를 년, 월, 일로 구분!
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day


df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')


df.set_index('new_Date', inplace=True)
print(df.head(3))
print(df.index)
# DatetimeIndex(['2018-07-02', '2018-06-29', '2018-06-28', '2018-06-27',
#                '2018-06-26', '2018-06-25', '2018-06-22', '2018-06-21',
#                '2018-06-20', '2018-06-19', '2018-06-18', '2018-06-15',
#                '2018-06-14', '2018-06-12', '2018-06-11', '2018-06-08',
#                '2018-06-07', '2018-06-05', '2018-06-04', '2018-06-01'],
#               dtype='datetime64[ns]', name='new_Date', freq=None)

# 날짜 인덱스를 이용하여 데이터 선택하기
df_y = df['2018'] # 날짜 인덱스를 사용하면 연-월-일 중에서 내가 필요로 하는 레벨을 선택적으로 인덱싱할 수 있다.
print(df_y) # 2018년도에 해당하는 모든 행을 선택
print(df.loc['2018-07', 'Date':'Date_m'])
print(df.loc['2018-06-25':'2018-06-20'])
#                   Date  Close  Start   High    Low  Volume  Year  Month  Day Date_yr   Date_m
# new_Date
# 2018-07-02  2018-07-02  10100  10850  10900  10000  137977  2018      7    2    2018  2018-07
#                   Date  Close  Start   High    Low  Volume  Year  Month  Day Date_yr   Date_m
# new_Date
# 2018-06-25  2018-06-25  11150  11400  11450  11000   55519  2018      6   25    2018  2018-06
# 2018-06-22  2018-06-22  11300  11250  11450  10750  134805  2018      6   22    2018  2018-06
# 2018-06-21  2018-06-21  11200  11350  11750  11200  133002  2018      6   21    2018  2018-06
# 2018-06-20  2018-06-20  11550  11200  11600  10900  308596  2018      6   20    2018  2018-06
today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
print(df['time_delta'][0])
df.set_index('time_delta', inplace=True)
df_180 = df['180 days':'189 days']
print(df_180.head(5))