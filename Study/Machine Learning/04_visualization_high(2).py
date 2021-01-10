import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
sns.set_style('whitegrid')


#빈도 그래프(동일 오류 출력)
# UserWarning: 14.3% of the points cannot be placed; you may want to decrease the size of the markers or use stripplot.
# fig = plt.figure(figsize=(30, 10))
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1, 3, 3)

# #기본값
# sns.countplot(x="class", palette="Set1", data=titanic, ax= ax1)

# #hue옵션에 who 추가
# sns.countplot(x="class", hue= 'who', palette="Set2", data=titanic, ax= ax2)

# #dodge=FALSE 옵션 추가(축 방향으로 분리하지 않고 누적 그래프 출력)
# sns.countplot(x="class", dodge= False, palette="Set3", data=titanic, ax= ax3)

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


#박스플롯 바이올린 그래프
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

sns.boxplot(x='alive', y='age', data=titanic, ax = ax1) #기본값
sns.boxplot(x='alive', y='age', hue='sex',data=titanic, ax = ax2) #hue변수 추가
sns.violinplot(x='alive', y='age', data=titanic, ax = ax3) #기본값
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax = ax4) #hue변수 추가
plt.show()


#조인트 그래프 만들기
j1 = sns.jointplot(x='fare', y='age', data=titanic) #산점도 기본값
j2 = sns.jointplot(x='fare', y='age', kind= 'reg', data=titanic) #회귀선
j3 = sns.jointplot(x='fare', y='age', kind= 'hex', data=titanic) #육각 그래프
j4 = sns.jointplot(x='fare', y='age', kind= 'kde', data=titanic) #커럴 밀집 그래프

j1.fig.suptitle("산점도 기본값")
j2.fig.suptitle("회귀선")
j3.fig.suptitle("육각")
j4.fig.suptitle("커럴 밀집 그래프")
plt.show()

#조건을 적용하여 화면을 그리드로 분할하기
g = sns.FacetGrid(data=titanic, col='who', row='survived')
g = g.map(plt.hist, 'age')
plt.show()

#이변수 데이터의 분포
titanic_pair = titanic[['age', 'pclass', 'fare']]
g = sns.pairplot(titanic_pair)
plt.show()

