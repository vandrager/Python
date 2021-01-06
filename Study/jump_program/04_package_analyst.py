import numpy as np

discount = 0.05
cashflow = 100
def presentvalue(n):
    return (cashflow/((1+discount)**n))

print(presentvalue(3))

loss = [-750, -250]
profit = [100]*18
cf = loss + profit
print(len(cf))
cashflow = np.array(cf)
print(np.npv(0.045, cashflow))
print(np.irr(cashflow))

npv = np.npv(0.045, cashflow)
irr = np.irr(cashflow)

import pandas as pd

data = {'name': ['mark', 'jane', 'mattew', 'ryan'],
        'age': [33, 42, 44, 39],
        'score': [91.3, 89.2, 95.3, 93.8]}

df = pd.DataFrame(data)
print(df)
print(df.sum())
print(df.mean())
print(df.age)

import re, os
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')

# 판다스로 csv파일을 불러올 때는 read_csv함수를 사용 --> 자동으로 데이터 프레임으로 변환됨
data = pd.read_csv('아파트(매매)__실거래가_20210105153210.csv', encoding='euc-kr')
print(len(data))
print(data[:5])
print(data.head(10))
print(data.tail(10))
print(data[(data.면적 > 100) & (data.면적 < 120)]) # and 조건 결합
print(data[(data.면적 > 100) | (data.면적 < 120)]) # or 조건 결합

# 원하는 자료만 살펴보려면?
print(data.loc[:10, ['시군구', '거래금액']])
print(data.loc[:10, ['시군구', '거래금액']][(data.면적 > 80) | (data.면적 < 80)])
print(data.loc[:, ['시군구', '단지명', '면적', '거래금액']][(data.면적 > 200)])

# 판다스에서 쉼표가 있는 문자를 숫자로 한 번에 바꾸는 방법
data.거래금액 = data.거래금액.str.replace(',', '').astype('int64')
print(data.loc[:10, ['시군구', '거래금액']])

# 새로운 값 추가하기
data['단가'] = data.거래금액 / data.면적
print(data.loc[:10, ['단지명', '면적', '거래금액', '단가']])

print(data.sort_values(by = '거래금액', ascending = False).loc[:, ['단지명', '거래금액']]) # 내림차순

# 특정한 문자를 포함하는 열 추출하기
print(data.head())
print(data.시군구.str.find("부산"))
# 찾았으면 인덱스 값을, 찾지 못했으면 -1을 출력한다.
busan = data[data.시군구.str.find("부산광역시") > -1]
print(busan)

df2 = pd.read_csv('survey.csv')
print(df2.head())
print(df2.mean())
print(df2.income.mean())
print(df2.income.median()) #중앙값
print(df2.describe()) #기초통계량
print(df2.income.value_counts())
print(df2.sex.value_counts())
print(df2.groupby(df2.sex).mean())

cor = df2.corr(method='spearman') # 기본 분석은 pearson, spearman분석도 사용 가능
print(cor)
# cor2 = df2.stress.corr(df2.income)
# print(cor2)
# busan.to_csv("busan.csv")

# 회귀분석 실습
# pip install statmodels
import statsmodels.formula.api as smf
model = smf.ols(formula = 'jobSatisfaction~English', data = df2)
result = model.fit()
print(result.summary())

model2 = smf.ols(formula = 'jobSatisfaction~English+income+stress', data = df2)
result2 = model2.fit()
print(result2.summary())