import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")
from matplotlib import font_manager, rc
font_path = r'C:\Windows\Fonts\Malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_excel('시도별 전출입 인구수.xlsx', header=0)
df = df.fillna(method = 'ffill')


# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis =1)
df_seoul.rename({'전입지별': '전입지'}, axis =1, inplace = True)
df_seoul.set_index('전입지', inplace = True)

col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
df_4 = df_4.T

plt.style.use("ggplot")
df_4.index = df_4.index.map(int)


df_4.plot(kind='bar', width = 0.7, figsize=(20, 10),
        color=['orange', 'green', 'skyblue', 'blue'])

plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size= 20)
plt.xlabel('기간', size= 20)
plt.ylim(5000, 30000)
plt.legend(loc="best", fontsize= 20)
plt.show()

# 가로 막대그래프 그려보자보자
col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
df_4['합계'] = df_4.sum(axis=1)
df_total = df_4[['합계']].sort_values(by="합계", ascending=True)
plt.style.use("ggplot")
df_total.plot(kind='barh', color='cornflowerblue', width = 0.5, figsize=(10, 5))
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('전입지', size= 20)
plt.xlabel('기간', size= 20)
plt.show()