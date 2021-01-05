import csv, os, usecsv
import re
print(os.getcwd())
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")

newpop = usecsv.opencsv("popseoul.csv")
for n in newpop:
    print(n)

for i in newpop:
    for j in i:
        try:
            i[i.index(j)] = float(re.sub(',', '', j))
        except:
            pass
    
# for pop in newpop:
#     print(pop)

# 자치구[0] 전체 합계 [2] 한국인 계 [5] 등록외국인 계 [8] 

print("{}%".format(round((newpop[2][8]/newpop[2][2])*100, 2)))
for i in newpop:
    foreign = 0
    try:
        foreign = round((i[8]/i[2])*100, 2)
        if foreign >= 3:
            print("{} {}%".format(i[0], foreign))
    except:
        pass

new = [['구', '한국인', '외국인', '합계', '외국인비율(%)']]
# 자치구[0] 전체 합계 [2] 한국인 계 [5] 등록외국인 계 [8] 

for i in newpop:
    foreign = 0
    try:
        foreign = round((i[8]/i[2])*100, 2)
        if foreign >= 3:
            print("{} {}%".format(i[0], foreign))
            new.append([i[0], i[5], i[8], i[2], foreign])
    except:
        pass

for n in new:
    print(n)

usecsv.writecsv('new.csv', new)

