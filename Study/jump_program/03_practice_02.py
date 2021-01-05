import os, csv, usecsv
import re
print(os.getcwd())
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
print(os.getcwd())

# word = usecsv.opencsv('2020.12.26_이슈키워드.csv')
# for w in word:
#     print(w)

list_b = [["yb", "intro", "miss-a", 'volumeup'], ["123", "234", "345", "632"]]
list_c = usecsv.writecsv('bigdata.csv', list_b)

total = usecsv.opencsv('전국마을기업표준데이터.csv')
# for t in total:
#     print(t)

# j = '1,468,345'
# print(float(re.sub(',', '', j)))
# print(j)
# print(type(float(re.sub(',', '', j))))

# i = total[2]
# print(i) #67
# k = []
# for j in i:
#     if re.search(r'[a-z가-힣-]', j): # 알파벳 또는 한글, -가 있다면 그대로 넣어버려라
#         k.append(j)

#     elif j == '': #공백이면 묻따 그냥 넣어부리라
#         k.append(j)
    
#     else:
#         k.append(float(re.sub(',', '', j)))


# 한글만 가능 : [ 가나다라 ... ] 주의 : ㄱㄴㄷ... 형식으로는 입력 불가능 , 띄어쓰기 불가능
# /^[가-힣]+$/

# 한글,띄어쓰기만 가능 : [ 가나다라 ... ] 주의 : ㄱㄴㄷ... 형식으로는 입력 불가능 , 띄어쓰기 가능
# /^[가-힣\s]+$/


# print(k)

i = total[3]
for j in i:
    try:
        i[i.index(j)] = float(re.sub(',', '', j)) # 모든 j를 실수형으로 바꿔준다.
    except: # 오류가 발생하면 pass를 사용해 그냥 넘어감
        pass

print(i)

for t in total:
    for p in t:
        try:
            t[t.index(p)] = float(re.sub(',', '', j))
        except:
            pass

print(total)