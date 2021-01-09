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

col_years = list(map(str, range(1970, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
df_4 = df_4.T

plt.style.use("ggplot")
# 데이터 프레임의 인덱스를 정수형으로 변경(x축 눈금 라벨 표시)
df_4.index = df_4.index.map(int)

#면적 그래프 그리기(stacked=False)
df_4.plot(kind='area', stacked=False, alpha=0.2, figsize=(20, 10))
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size= 20)
plt.xlabel('기간', size= 20)
plt.legend(loc="best", fontsize= 20)
plt.show()

#누적 면적 그래프 그리기(stacked=True)
df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size= 20)
plt.xlabel('기간', size= 20)
plt.legend(loc="best", fontsize= 20)
plt.show()

#axes객체 속성 변경하기
ax = df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))
print(type(ax))
ax.set_title('서울 -> 타시도 인구 이동', size=30, color='brown', weight="bold")
ax.set_ylabel('이동 인구 수', size= 20, color='blue')
ax.set_xlabel('기간', size= 20)
ax.legend(loc="best", fontsize= 20)
plt.show()