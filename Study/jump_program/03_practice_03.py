import csv, re, os, usecsv

os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
print(os.getcwd())

apt = usecsv.opencsv('아파트(매매)__실거래가_20210105153210.csv')
for i in apt:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(',', '', j))
        except:
            pass


for a in apt[:5]:
    print(a)

print(len(apt))

# Q. 120 제곱 미터 이상 3억원 이하인 강원도의 아파트를 찾아보자보자

print(apt[1][0][0:3])
# [6] 전용면적 [9] 거래금액
want = [['위치', '전용면적', '거래금액']]
for k in apt:
    try:
        if k[0][0:3] == '강원도' and k[5] >= 120 and k[8] >= 30000:
           want.append([k[0], k[5], k[8]])
    except:
        pass


print(want)
usecsv.writecsv("wantapt.csv", want)