import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")
# poy = pd.DataFrame([[1, 2, 3, 4],
#                     [2, 3, 4, 5]],
#                     index=['용숙', '소라'],
#                     columns=['원', '투', '쓰리', '뽀!'])

# print(poy)
# poy['파이브'] = [5, 6]
# print(poy)
# poy.loc['비버'] = [1, 2, 3, 4, 5]
# print(poy)
# print(poy.loc['소라':'비버', '쓰리':'파이브'])
# popo = poy.loc['소라':'비버', '쓰리':'파이브']
# popo.to_csv("popo.csv")

df = pd.read_excel('시도별 전출입 인구수.xlsx', header=0)
print(df.head(5))

# 누락값 NAN을 앞 데이터로 채움(엑셀 양식 병합 부분)
df = df.fillna(method = 'ffill')
print(df.head(5))

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis =1)
df_seoul.rename({'전입지별': '전입지'}, axis =1, inplace = True)
df_seoul.set_index('전입지', inplace = True)
print(df_seoul)

sr_one = df_seoul.loc['경기도']
print(sr_one) #sr_one 이라는 시리즈 형태를 출력해줌
print(type(sr_one)) # <class 'pandas.core.series.Series'>

# 한글 폰트 오류 해결 방법
from matplotlib import font_manager, rc
font_path = r'C:\Windows\Fonts\Malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
print(plt.style.available)
# 맷플롯립 스타일은 여기 사이트 참고 ("https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html")
plt.style.use('seaborn-pastel') # 스타일 서식 지정
plt.figure(figsize=(14, 5)) # 가로 14 세로 5인치
plt.xticks(rotation='vertical') # x축 수직으로 전환
plt.plot(sr_one.index, sr_one.values, marker = 'o', markersize=5) #series는 인덱스와 밸류 값으로 구분, marker 추가
plt.title('서울(전출) --> 경기(전입)') #제목 설정
plt.xlabel("연도") # 축 이름 만들기
plt.ylabel("유입수") # 축 이름 만들기
plt.legend(labels= ['서울 -> 경기'], loc='best', fontsize = 15) # 범례 표시
plt.show()
# plt.ylim(50000, 80000) #y축 범위 지정
# 그래프에 대한 설명(주석) 첨부 방법 근데 또 안먹힘^^...
# plt.annotate('',
#             xy=(20, 620000),
#             xytext=(2, 290000),
#             xycoords='data',
#             arrowprops=dict(arrowstyle='->', color="skyblue", lw=5),
#             )
# plt.annotate('',
#             xy=(47, 450000),
#             xytext=(30, 580000),
#             xycoords='data',
#             arrowprops=dict(arrowstyle='->', color="olive", lw=5),
#             )
# plt.annotate('인구 이동 증가(1970~)',
#             xy=(10, 550000),
#             rotation=25,
#             va='baseline',
#             ha='center',
#             fontsize=15,
#             )
# plt.annotate('인구 이동 증가(1995~)',
#             xy=(40, 560000),
#             rotation=11,
#             va='baseline',
#             ha='center',
#             fontsize=15,
#             )

# 화면 분할하여 그래프 여러개 그리기
# 그래프 객체 생성 figure에 2개의 서브 플롯 생성
fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# axe객체에 plot함수로 그래프 출력
ax1.plot(sr_one, 'o', markersize =5)
ax2.plot(sr_one, marker='o', markersize =5, markerfacecolor='green',
        color='olive', linewidth=2, label='서울 -> 경기')
ax2.legend(loc='best')

#y축 범위 지정(최소값, 최대값)
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

#축 눈금 라벨 지정 및 75도 회전
ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)
plt.show()


# ---------------------> 한글 폰트 깨짐 문제 발생
# plt.plot(sr_one.values, sr_one.index)
# plt.show()

# 설치된 폰트 출력
# import matplotlib.font_manager as fonm
# font_list = [font.name for font in fonm.fontManager.ttflist]
# for f in font_list:
#     print(f"{f}.ttf")

col_years = list(map(str, range(1970, 2018)))
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도'], col_years]

plt.style.use('Solarize_Light2')
fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(1, 1, 1)

ax.plot(col_years, df_3.loc['충청남도',:], marker='o', markersize =5, markerfacecolor='green',
        color='olive', linewidth=2, label='서울 -> 충남')
ax.plot(col_years, df_3.loc['경상북도',:], marker='o', markersize =5, markerfacecolor='blue',
        color='skyblue', linewidth=2, label='서울 -> 경북')
ax.plot(col_years, df_3.loc['강원도',:], marker='o', markersize =5, markerfacecolor='red',
        color='magenta', linewidth=2, label='서울 -> 강원')
ax.legend(loc='best')
#차트 제목 추가
ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20)

#축 이름 추가
ax.set_xlabel('연도', size=10)
ax.set_ylabel('인구수', size=10)

#축 눈금 라벨 지정 및 90도 회전
ax.set_xticklabels(col_years, rotation=90)

# 축 눈금 라벨 크기
ax.tick_params(axis="x", labelsize=10)
ax.tick_params(axis="y", labelsize=10)
plt.show()

col_years = list(map(str, range(1970, 2018)))
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

plt.style.use('seaborn-deep')
fig = plt.figure(figsize=(20, 20))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.plot(col_years, df_3.loc['충청남도',:], marker='o', markersize =5, markerfacecolor='green',
        color='olive', linewidth=2, label='서울 -> 충남')
ax2.plot(col_years, df_3.loc['경상북도',:], marker='o', markersize =5, markerfacecolor='blue',
        color='skyblue', linewidth=2, label='서울 -> 경북')
ax3.plot(col_years, df_3.loc['강원도',:], marker='o', markersize =5, markerfacecolor='red',
        color='magenta', linewidth=2, label='서울 -> 강원')
ax4.plot(col_years, df_3.loc['전라남도',:], marker='o', markersize =5, markerfacecolor='purple',
        color='yellow', linewidth=2, label='서울 -> 전남')
ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')
#차트 제목 추가
ax1.set_title('서울 -> 충남 인구 이동', size=20)
ax2.set_title('서울 -> 경북 인구 이동', size=20)
ax3.set_title('서울 -> 강원 인구 이동', size=20)
ax4.set_title('서울 -> 전남 인구 이동', size=20)

#축 눈금 라벨 지정 및 90도 회전
ax1.set_xticklabels(col_years, rotation=90)
ax2.set_xticklabels(col_years, rotation=90)
ax3.set_xticklabels(col_years, rotation=90)
ax4.set_xticklabels(col_years, rotation=90)

plt.show()

import matplotlib
for c in matplotlib.colors.cnames.items():
        print(c)

# matplotlib color list
# ('aliceblue', '#F0F8FF')
# ('antiquewhite', '#FAEBD7')
# ('aqua', '#00FFFF')
# ('aquamarine', '#7FFFD4')
# ('azure', '#F0FFFF')
# ('beige', '#F5F5DC')
# ('bisque', '#FFE4C4')
# ('black', '#000000')
# ('blanchedalmond', '#FFEBCD')
# ('blue', '#0000FF')
# ('blueviolet', '#8A2BE2')
# ('brown', '#A52A2A')
# ('burlywood', '#DEB887')
# ('cadetblue', '#5F9EA0')
# ('chartreuse', '#7FFF00')
# ('chocolate', '#D2691E')
# ('coral', '#FF7F50')
# ('cornflowerblue', '#6495ED')
# ('cornsilk', '#FFF8DC')
# ('crimson', '#DC143C')
# ('cyan', '#00FFFF')
# ('darkblue', '#00008B')
# ('darkcyan', '#008B8B')
# ('darkgoldenrod', '#B8860B')
# ('darkgray', '#A9A9A9')
# ('darkgreen', '#006400')
# ('darkgrey', '#A9A9A9')
# ('darkkhaki', '#BDB76B')
# ('darkmagenta', '#8B008B')
# ('darkolivegreen', '#556B2F')
# ('darkorange', '#FF8C00')
# ('darkorchid', '#9932CC')
# ('darkred', '#8B0000')
# ('darksalmon', '#E9967A')
# ('darkseagreen', '#8FBC8F')
# ('darkslateblue', '#483D8B')
# ('darkslategray', '#2F4F4F')
# ('darkslategrey', '#2F4F4F')
# ('darkturquoise', '#00CED1')
# ('darkviolet', '#9400D3')
# ('deeppink', '#FF1493')
# ('deepskyblue', '#00BFFF')
# ('dimgray', '#696969')
# ('dimgrey', '#696969')
# ('dodgerblue', '#1E90FF')
# ('firebrick', '#B22222')
# ('floralwhite', '#FFFAF0')
# ('forestgreen', '#228B22')
# ('fuchsia', '#FF00FF')
# ('gainsboro', '#DCDCDC')
# ('ghostwhite', '#F8F8FF')
# ('gold', '#FFD700')
# ('goldenrod', '#DAA520')
# ('gray', '#808080')
# ('green', '#008000')
# ('greenyellow', '#ADFF2F')
# ('grey', '#808080')
# ('honeydew', '#F0FFF0')
# ('hotpink', '#FF69B4')
# ('indianred', '#CD5C5C')
# ('indigo', '#4B0082')
# ('ivory', '#FFFFF0')
# ('khaki', '#F0E68C')
# ('lavender', '#E6E6FA')
# ('lavenderblush', '#FFF0F5')
# ('lawngreen', '#7CFC00')
# ('lemonchiffon', '#FFFACD')
# ('lightblue', '#ADD8E6')
# ('lightcoral', '#F08080')
# ('lightcyan', '#E0FFFF')
# ('lightgoldenrodyellow', '#FAFAD2')
# ('lightgray', '#D3D3D3')
# ('lightgreen', '#90EE90')
# ('lightgrey', '#D3D3D3')
# ('lightpink', '#FFB6C1')
# ('lightsalmon', '#FFA07A')
# ('lightseagreen', '#20B2AA')
# ('lightskyblue', '#87CEFA')
# ('lightslategray', '#778899')
# ('lightslategrey', '#778899')
# ('lightsteelblue', '#B0C4DE')
# ('lightyellow', '#FFFFE0')
# ('lime', '#00FF00')
# ('limegreen', '#32CD32')
# ('linen', '#FAF0E6')
# ('magenta', '#FF00FF')
# ('maroon', '#800000')
# ('mediumaquamarine', '#66CDAA')
# ('mediumblue', '#0000CD')
# ('mediumorchid', '#BA55D3')
# ('mediumpurple', '#9370DB')
# ('mediumseagreen', '#3CB371')
# ('mediumslateblue', '#7B68EE')
# ('mediumspringgreen', '#00FA9A')
# ('mediumturquoise', '#48D1CC')
# ('mediumvioletred', '#C71585')
# ('midnightblue', '#191970')
# ('mintcream', '#F5FFFA')
# ('mistyrose', '#FFE4E1')
# ('moccasin', '#FFE4B5')
# ('navajowhite', '#FFDEAD')
# ('navy', '#000080')
# ('oldlace', '#FDF5E6')
# ('olive', '#808000')
# ('olivedrab', '#6B8E23')
# ('orange', '#FFA500')
# ('orangered', '#FF4500')
# ('orchid', '#DA70D6')
# ('palegoldenrod', '#EEE8AA')
# ('palegreen', '#98FB98')
# ('paleturquoise', '#AFEEEE')
# ('palevioletred', '#DB7093')
# ('papayawhip', '#FFEFD5')
# ('peachpuff', '#FFDAB9')
# ('peru', '#CD853F')
# ('pink', '#FFC0CB')
# ('plum', '#DDA0DD')
# ('powderblue', '#B0E0E6')
# ('purple', '#800080')
# ('rebeccapurple', '#663399')
# ('red', '#FF0000')
# ('rosybrown', '#BC8F8F')
# ('royalblue', '#4169E1')
# ('saddlebrown', '#8B4513')
# ('salmon', '#FA8072')
# ('sandybrown', '#F4A460')
# ('seagreen', '#2E8B57')
# ('seashell', '#FFF5EE')
# ('sienna', '#A0522D')
# ('silver', '#C0C0C0')
# ('skyblue', '#87CEEB')
# ('slateblue', '#6A5ACD')
# ('slategray', '#708090')
# ('slategrey', '#708090')
# ('snow', '#FFFAFA')
# ('springgreen', '#00FF7F')
# ('steelblue', '#4682B4')
# ('tan', '#D2B48C')
# ('teal', '#008080')
# ('thistle', '#D8BFD8')
# ('tomato', '#FF6347')
# ('turquoise', '#40E0D0')
# ('violet', '#EE82EE')
# ('wheat', '#F5DEB3')
# ('white', '#FFFFFF')
# ('whitesmoke', '#F5F5F5')
# ('yellow', '#FFFF00')
# ('yellowgreen', '#9ACD32')

