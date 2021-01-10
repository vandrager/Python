import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")

plt.style.use("default")
df = pd.read_csv("auto-mpg.csv", header=None)
df.columns = ["mpg", "cyl", "dis", "hor", "wei", "acc", "model", "origin", "name"]

#데이터 개수 카운트를 위해 값 1을 가진 열 추가
df['count'] = 1
df_origin = df.groupby('origin').sum() #origin 열을 기준으로 그룹화, 합계 계산
print(df_origin)
#            mpg   cyl      dis       wei     acc  model  count
# origin
# 1       5000.8  1556  61229.5  837121.0  3743.4  18827    249
# 2       1952.4   291   7640.0  169631.0  1175.1   5307     70
# 3       2405.6   324   8114.0  175477.0  1277.6   6118     79

#제조국가(origin)값을 실제 지역명으로 변경하기
df_origin.index = ['USA', 'EU', 'JPN']

# origin 열에 대한 파이 차트 그리기 -count data 사용
df_origin['count'].plot(kind = 'pie', autopct="%1.1f%%", startangle=10,
                        colors= ['coral', 'bisque', 'cadetblue'], figsize=(7, 5))
plt.title("model origin", size = 20)
plt.legend(labels = df_origin.index, loc='upper left')
plt.show()

# boxplot 만들기
from matplotlib import font_manager, rc
font_path = r'C:\Windows\Fonts\Malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use("seaborn-poster")
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.boxplot(x=[df[df['origin']==1]['mpg'],
                df[df['origin']==2]['mpg'],
                df[df['origin']==3]['mpg']],
                labels=['USA', 'EU', 'JPN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
                df[df['origin']==2]['mpg'],
                df[df['origin']==3]['mpg']],
                labels=['USA', 'EU', 'JPN'],
                vert=False)

ax1.set_title("박스플롯 세로version")
ax2.set_title("박스플롯 가로version")
plt.show()
# 파이썬 그래프 갤러리 다양한 그래프 모양과 설정 옵션을 참조할 수 있음!
# https://python-graph-gallery.com/