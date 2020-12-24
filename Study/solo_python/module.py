import math

print(math.sin(1))

from math import *
print(sin(1))
print(cos(1))

import random as rd
#0부터 1사이의 float을 리턴합니다.
print(rd.random())
#uniform(min, max) 지정한 범위 사이의 float을 리턴합니다.
print(rd.uniform(10, 200))
#randrange 지정한 범위의 int를 리턴합니다.
# randrange(max) 0부터 max까지
# randrange(min, max) min부터 max까지
print(rd.randrange(170, 190))

#choice(list) 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
list_b = [1, 2, 34, 35, 32]
print(rd.choice(list_b))

#shuffle(list) 리스트의 요소들을 랜덤하게 섞습니다.
print(rd.shuffle(list_b))
print(list_b)

#sample(list, k = <숫자>) 리스트의 요소 중에 k개를 뽑습니다.
print(rd.sample(list_b, 2))
import sys
print(sys.argv)
print(sys.getwindowsversion)
print(sys.copyright)
print(sys.version)

print(sys.argv)

import os
print(os.name)
print(os.getcwd())
print(os.listdir())
os.mkdir("hello")
os.rmdir("hello")
with open("original.txt", 'w') as file:
    file.write("hello")
os.rename("original.txt", "new.txt")
os.remove("new.txt")
os.system("dir")

import datetime
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
#now.strfttime 할 때 월일을 뜻하는 m, d는 반드시 소문자로 작성해야 정상 출력됨, 대문자는 인식X
print(now.strftime("%Y, %M, %D, %H, %M, %S"))
out = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
print(out)
#특정 시간 이후의 시간 구하기
after = now + datetime.timedelta(\
    weeks=1, \
    days=1, \
    hours=1,\
    minutes=1, \
    seconds=1)

print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

#특정 시간 요소 교체하기
out_2 = now.replace(year=(now.year + 1))
print(out_2.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

import time
time.sleep(5)
print("program exit")
from urllib import request
target = request.urlopen("http://google.com")
out_3 = target.read()
print(out_3)