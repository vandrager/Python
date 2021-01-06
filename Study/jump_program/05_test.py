import numpy as np

e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e)
zero = np.zeros((2, 4))
one = np.ones((2, 4))
print(zero)
print(one)
# np.transpose 행열바꾸기
np.transpose(one)
print(np.transpose(one))
cf = np.array([-400, -200, 300, 300, 300, 300])
flow = np.irr(cf)
print(flow)
discount = 0.055
print(np.npv(discount, cf))

import pandas as pd
data = {'name': ['marry', 'kane', 'ryan', 'bony'],
        'age': [33, 42, 44, 83],
        'score': [91.4, 89.6, 75.5, 90.3]}
df = pd.DataFrame(data)
print(df.age.mean())
print(df.score.sum())
print(df.describe())
print(df.name[(df.age > 40) & (df.score > 80)])
print(df.sort_values('score', ascending=False))
print(df[(df.name.str.find("a") > -1)])
print(df.corr())