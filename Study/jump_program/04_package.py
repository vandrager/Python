# 설치된 패키지 확인법
# 터미널에서 pip list 입력


import numpy as np
a = np.array([[2, 3], [5, 2]])
print(a)
# [[2 3]
#  [5 2]]
b = np.array([[1, 2, 3, 4, 5], [3, 4, 5, 6, 7], [5, 6, 7, 8, 9]])
print(b)
# [[1 2 3 4 5]
#  [3 4 5 6 7]
#  [5 6 7 8 9]]
print(b[1][2])
print(b[1, 2])
print(b[1:, 3:])
print(b.shape)
# 5
# 5
# [[6 7]
#  [8 9]]
# (3, 5)
print(b.dtype) # 배열의 원소 유형 확인하기
# int32(정수로 이뤄졌다는 뜻)
b.astype('float64') # 배열 유형 바꾸기
print(np.zeros((2, 10)))
print(np.ones((2, 10)))
print(5*np.ones((2, 10)))
print(np.arange(2, 10)) # 2이상 10 미만의 원소로 이루어진 1차원 배율을 만듭니다.
p = np.ones((2, 5))
q = np.transpose(p)
print(q.dtype)
q.astype('int64')
print(q.dtype)

np1 = np.array([[1, 2, 3], [4, 5, 6], [7, 5, 3]])
np2 = np.array([[4, 5, 2], [8, 3, 1], [7, 5, 3]])
print(np1+np2)
print(np1-np2)
print(np1*np2)
print(np1/np2)
np3 = np.array([[100], [200], [300]])
print(np1 + np3)

a = [1, 2, 3]
print(type(np1))
print(type(a))
# <class 'numpy.ndarray'>
# <class 'list'>
print(np1*a)
# 그냥 리스트랑 배열이랑 계산해도 브로드캐스팅이 되넹?ㅅ?

np1 = np.array([[1, 2, 3], [4, 5, 6], [7, 5, 3]])
np1[1:2, 1:3] = 0
# [[ 1  4  9]
#  [ 4 10 18]
#  [ 7 10  9]]
# [[1 2 3]
#  [4 0 0]
#  [7 5 3]]
print(np1)

np4 = np.arange(10)
np4[:5]
np4[-5:]
print(np1[:, 2])

import csv, usecsv, re, os

os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
q = usecsv.opencsv('quest.csv')
for i in q:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(',', '', j))
        except:
            pass

quest = np.array(q)
print(quest.dtype)

print(quest > 4)
quest[quest > 5] = 5
quest[quest <= 0] = 1
print(quest)
usecsv.writecsv('quest_final.csv', quest)
