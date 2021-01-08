#pip install scipy
#pip install scikit-learn
import pandas as pd
import numpy as np
import csv, usecsv, os, re
import seaborn as sns
dict_data = {'a': 1, "b": 2, "c": 3}
k = pd.Series(dict_data) # 시리즈는 1:1대응
print(k)
list_data = [10, 100, 1000, 10000]
k = pd.Series(list_data, index=["동전", "동전2", "지폐", "지폐2"])
print(k['동전'])


os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
data = pd.read_csv("아파트(매매)__실거래가_20210105153210.csv", encoding="euc-kr")
print(data.head(5))

d = {"name": ['henry', 'shine', 'ryan'],
    "height": [171, 180, 165],
    "weight": [80, 90, 100]}

df = pd.DataFrame(d)
print(df)

df2 = pd.DataFrame([['영어', '역북초', 390],
                    ['수학', '신갈초', 360],
                    ['과학', '수지초', 400]],
                    index=['진솔', '영화', '휘재'],
                    columns=["과목", "출신초교", "수능점수"])

# 판다스 열이름, 인덱스 변경하는 법 + inplace=True를 옆에 넣어줘야 바뀐다 임마!
df2.rename(columns={"과목": "자신있는 과목", "출신초교": "출신학교", "수능점수": "받아쓰기점수"}, inplace=True)
df2.rename(index={"진솔": "학생1", "영화": "학생2", "휘재": "학생3"}, inplace=True)
print(df2)

# 판다스 행/열 삭제하기
df2.drop("학생3", axis=0, inplace=True) #행 삭제
df2.drop("받아쓰기점수", axis=1, inplace=True) #열 삭제
print(df2)
#     자신있는 과목 출신학교  받아쓰기점수
# 학생1      영어  역북초     390
# 학생2      수학  신갈초     360
# 학생3      과학  수지초     400
#     자신있는 과목 출신학교
# 학생1      영어  역북초
# 학생2      수학  신갈초

df2.rename(columns={"자신있는 과목": "과목"}, inplace=True)
df2.rename(index={"학생1": "수원"}, inplace=True)
print(df2)
#      과목 출신학교
# 수원   영어  역북초
# 학생2  수학  신갈초

df = pd.DataFrame([[90, 80, 70], [98, 89, 95], [85, 74, 25], [94, 25, 85]],
                    columns=['수학', '영어', '도덕'],
                    index=['민지', '설아', '수지', '초아'])
print(df)

#행만 선택해서 출력하기
label1 = df.loc['민지']
position1 = df.iloc[0]
print(label1, '\n')
print(position1)

label2 = df.loc[['민지', '설아']]
print(label2)
position2 = df.iloc[[0, 1]]
print(position2)
print(df.iloc[::2])
print(df.iloc[::-1]) #역순으로 출력하기
#     수학  영어  도덕
# 민지  90  80  70
# 설아  98  89  95
#     수학  영어  도덕
# 민지  90  80  70
# 설아  98  89  95
#     수학  영어  도덕
# 민지  90  80  70
# 수지  85  74  25
#     수학  영어  도덕
# 초아  94  25  85
# 수지  85  74  25
# 설아  98  89  95
# 민지  90  80  70

#열만 선택해서 출력하기
print(df['수학'])
print(df.도덕)
# 민지    90
# 설아    98
# 수지    85
# 초아    94
# Name: 수학, dtype: int64
# 민지    70
# 설아    95
# 수지    25
# 초아    85
# Name: 도덕, dtype: int64

df = pd.DataFrame([['민지', 90, 80, 70, 80], ['설아', 98, 89, 95, 90], ['수지', 85, 74, 25, 79], ['초아', 94, 25, 85, 88]],
                    columns=['이름', '수학', '영어', '도덕', '역사'])

df.set_index('이름', inplace=True)
print(df)

#     수학  영어  도덕
# 이름
# 민지  90  80  70
# 설아  98  89  95
# 수지  85  74  25
# 초아  94  25  85

label1 = df.loc['민지', ['영어', '도덕']]
position1 = df.iloc[0, [1, 2]]
print(label1, '\n')
print(position1)
# 영어    80
# 도덕    70
# Name: 민지, dtype: int64

# 영어    80
# 도덕    70
# Name: 민지, dtype: int64

#아래와 같이 슬라이싱도 가능
label1 = df.loc['민지', '도덕':'역사']
position1 = df.iloc[0, 2:4]
print(label1, '\n')
print(position1)
# 도덕    70
# 역사    80
# Name: 민지, dtype: int64

# 도덕    70
# 역사    80
# Name: 민지, dtype: int64

label1 = df.loc['민지', '영어':]
print(label1, '\n')
# 영어    80
# 도덕    70
# 역사    80
# Name: 민지, dtype: int64

position1 = df.iloc[0, 1:]
print(position1)
# 영어    80
# 도덕    70
# 역사    80
# Name: 민지, dtype: int64

label1 = df.loc[['민지', '초아'], '영어':]
print(label1, '\n')

position1 = df.iloc[[0, 3], 1:]
print(position1)
#    영어  도덕  역사
# 이름
# 민지  80  70  80
# 초아  25  85  88

#     영어  도덕  역사
# 이름
# 민지  80  70  80
# 초아  25  85  88

print(df)

df['과학'] = [90, 80, 98, 78]
print(df)
df.loc['재호'] = [ 20, 30, 40, 73, 92]
df.loc['코조'] = 0
df.loc['야로'] = df.loc['코조']
print(df)
#     수학  영어  도덕  역사  과학
# 이름
# 민지  90  80  70  80  90
# 설아  98  89  95  90  80
# 수지  85  74  25  79  98
# 초아  94  25  85  88  78
# 재호  20  30  40  73  92
# 코조   0   0   0   0   0
# 야로   0   0   0   0   0
df.loc['코조':'야로', 0:] = [[80, 90, 70, 50, 30], [90, 20, 40, 90, 80]]
print(df)
# 행열바꾸기
# df.transpose() or df.T
print(type(df))
df.transpose()
print(df.transpose())

# 인덱스 활용
# 행 인데스 재배열
new_name = ['설아', '재호', '수지', '초아', '용식', '근정']
ndf = df.reindex(new_name, fill_value = 0)
#       수학    영어    도덕    역사    과학
# 이름
# 설아  98.0  89.0  95.0  90.0  80.0
# 재호  20.0  30.0  40.0  73.0  92.0
# 수지  85.0  74.0  25.0  79.0  98.0
# 초아  94.0  25.0  85.0  88.0  78.0
# 용식   0   0   0   0   0
# 근정   0   0   0   0   0 --- > 없는 이름은 0으로 다 채워라

ndf = ndf.reset_index()
print(ndf)
#    이름  수학  영어  도덕  역사  과학
# 0  설아  98  89  95  90  80
# 1  재호  20  30  40  73  92
# 2  수지  85  74  25  79  98
# 3  초아  94  25  85  88  78
# 4  용식   0   0   0   0   0
# 5  근정   0   0   0   0   0
print(ndf.sort_index(ascending=False))
#    이름  수학  영어  도덕  역사  과학
# 5  근정   0   0   0   0   0
# 4  용식   0   0   0   0   0
# 3  초아  94  25  85  88  78
# 2  수지  85  74  25  79  98
# 1  재호  20  30  40  73  92
# 0  설아  98  89  95  90  80
print(ndf.sort_values('역사', ascending=False))
#    이름  수학  영어  도덕  역사  과학
# 0  설아  98  89  95  90  80
# 3  초아  94  25  85  88  78
# 2  수지  85  74  25  79  98
# 1  재호  20  30  40  73  92
# 4  용식   0   0   0   0   0
# 5  근정   0   0   0   0   0

# 산술연산
student = pd.Series({'국어': 100, "수학": 200, "영어": 300})
per = student/100
print(student)
print(per)
# 국어    100
# 수학    200
# 영어    300
# dtype: int64
# 국어    1.0
# 수학    2.0
# 영어    3.0
# dtype: float64

student1 = pd.Series({'국어': 100, "수학": 20, "영어": 30})
student2 = pd.Series({'국어': 60, "수학": 70, "영어": 50})
add = student1 + student2

minus = student1 - student2
division = student1 / student2
multiple = student1 * student2
all_data = pd.DataFrame([add, minus, division, multiple],
                        index=['덧셈', '뺄셈', '나눗셈', '곱셈'])
print(all_data)

student1 = pd.Series({'국어': np.nan, "수학": 20, "영어": 30})
student2 = pd.Series({'국어': 60, "수학": 70})

sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                        index=['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)
#        국어           수학    영어
# 덧셈   60.0    90.000000  30.0
# 뺄셈  -60.0   -50.000000  30.0
# 곱셈   0.0  1400.000000   0.0
# 나눗셈    0.0     0.285714   inf
# inf ---> infinity 무한대 80/0

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())
#     age     fare
# 0  22.0   7.2500
# 1  38.0  71.2833
# 2  26.0   7.9250
# 3  35.0  53.1000
# 4  35.0   8.0500
top_5 = df.head()
addition = df + 10
print(addition) #age와 fare 모두에 10씩 추가됨

topx2 = top_5 + top_5
print(topx2)
#     age      fare
# 0  44.0   14.5000
# 1  76.0  142.5666
# 2  52.0   15.8500
# 3  70.0  106.2000
# 4  70.0   16.1000

# -----> dataframe끼리 계산할 때 한 쪽이 nan이면 에러가 출력된다. 오류값이 없는지 반드시 확인
topx2['fare'] = (topx2['fare']/2)
print(topx2)
#     age     fare
# 0  44.0   7.2500
# 1  76.0  71.2833
# 2  52.0   7.9250
# 3  70.0  53.1000
# 4  70.0   8.0500
