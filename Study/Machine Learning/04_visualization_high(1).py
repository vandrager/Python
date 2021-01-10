import seaborn as sns
import matplotlib.pyplot as plt
# import warnings
# warnings.filterwarnings("ignore")

titanic = sns.load_dataset('titanic')

print(titanic.head())
print(titanic.info())

#스타일 테마 설정('darkgrid', 'whitegrid', 'dark', 'white', ticks)
sns.set_style('darkgrid')

#회귀선이 있는 산점도
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

sns.regplot(x= 'age',
            y= 'fare',
            data= titanic,
            ax = ax1)

sns.regplot(x= 'age',
            y= 'fare',
            data= titanic,
            ax = ax2,
            fit_reg=False) #회귀선 미표시

plt.show()

#히스토그램/커널 밀도 그래프
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

#기본값fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
sns.distplot(titanic['fare'], ax= ax1) #히스토그램과 커널 밀도 그래프를 표시

#hist = False
sns.distplot(titanic['fare'], hist=False, ax= ax2)

#kde = False
sns.distplot(titanic['fare'], kde=False, ax= ax3)

ax1.set_title('titanic fare - hist/ked')
ax2.set_title('titanic fare - ked')
ax3.set_title('titanic fare - hist')
plt.show()

#히트맵
#피벗 테이블로 범주형 변수를 각각 행, 열로 재구분하여 정리
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

sns.heatmap(table,
            annot=True, fmt='d',
            cmap='YlGnBu',
            linewidths=.5,
            cbar=False)

plt.show()

#범주형 데이터의 산점도 (에러가 뜸)
# UserWarning: 9.2% of the points cannot be placed; you may want to decrease the size of the markers or use stripplot.
#   warnings.warn(msg, UserWarning)

# sns.set_style('whitegrid')
# fig = plt.figure(figsize=(15, 5))
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)

# # 이산형 변수의 분포 - 데이터 분산 미고려
# sns.stripplot(x="class",
#               y='age',
#               data=titanic,
#               ax= ax1)

# # 이산형 변수의 분포 - 데이터 분산 고려(중복X)
# sns.swarmplot(x="class",
#               y='age',
#               data=titanic,
#               ax= ax2)

# ax1.set_title('stripplot')
# ax2.set_title('swarmplot')
# plt.plot()

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# x축 y축에 변수 할당
sns.barplot(x='sex', y='survived', data=titanic, ax = ax1)

# x축 y축에 변수 할당하고 hue옵션 추가
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax = ax2)

# x축 y축에 변수 할당하고 hue옵션 추가하고 누적 출력
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax = ax3)

ax1.set_title('titanic survived - sex')
ax2.set_title('titanic survived - sex/class')
ax3.set_title('titanic survived - sex/class(stacked)')
plt.show()