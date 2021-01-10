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

# 2축 그래프도 만들어보자
plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus'] = False #마이너스 부호 출력 설정
# convert_float=True 로 하면, 엑셀에 있는 숫자 데이터를 실수형(float)으로 변환합니다. 
df = pd.read_excel("남북한발전전력량.xlsx", convert_float=True)
df = df.loc[5:9]
df.drop("전력량 (억㎾h)", axis =1, inplace=True) #필요없는 열 삭제

df.set_index("발전 전력별", inplace=True)
df = df.T
# 발전 전력별   합계   수력   화력 원자력
# 1990    277  156  121   -
# 1991    263  150  113   -
# 1992    247  142  105   -

#증감률(변동률) 계산하기
df = df.rename(columns={'합계': "총발전량"}) #이름 변경
df['작년 총발전량'] = df['총발전량'].shift(1) #새로운 열을 만들고 총발전량의 열을 뒤로 한 칸씩 이동한 것으로 생성

# 발전 전력별 총발전량   수력   화력 원자력 작년 총발전량       증감률
# 1990    277  156  121   -     NaN       NaN
# 1991    263  150  113   -     277  -5.05415
# 1992    247  142  105   -     263  -6.08365
# 1993    221  133   88   -     247  -10.5263
# 1994    231  138   93   -     221   4.52489
df['증감률'] = ((df['총발전량']/df['작년 총발전량']) - 1) * 100
print(df)

#2축 그래프 그리기
ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True) #stacked=True 누적 그래프로 만들기
ax2 = ax1.twinx() #ax1객체의 쌍둥이 객체를 만들기 즉, 하나의 객체에서 다른걸 또 만들거임
ax2.plot(df.index, df.증감률, ls="--", marker='o', markersize=3, color= 'green', label="전년대비 증감률(%)")
# ls="--"옵션은 선 스타일을 점선으로 설정하는 명령임
ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량 (억㎾h)', size=10)
ax2.set_ylabel('전년대비 증감률(%)', size=10)
plt.title('북한 전력 발전량(1990~2016)', size=30)
ax1.legend(loc='best')
plt.show()

