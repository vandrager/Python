#pip install scipy
#pip install scikit-learn
import pandas as pd
import csv, usecsv, os, re
dict_data = {'a': 1, "b": 2, "c": 3}
k = pd.Series(dict_data)
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

# 판다스 열이름, 인덱스 변경하는 법 inplace=True를 옆에 넣어줘야 바뀐다 임마!
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



