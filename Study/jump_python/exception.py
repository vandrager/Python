4/1
a = [1, 2, 3]
print(a[2])

print(divmod(7, 3))


sum = lambda a, b: print("%d가 나왔습니다." %(a + b))
sum(10, 20)

k = [5, 10, 15, 20]
m = list(map(lambda a: a + 5, k))
print(list(map(lambda a: a + 5, k)))
print(max(k))
print(min(k))
print(m)

print(pow(2, 4))
print(2**4)

import os
os.chdir("C:\\Users\\vandr\\OneDrive\\바탕 화면\\Pythonworkspace")
print(os.getcwd())

import glob
print(glob.glob("C:\\Users\\vandr\\OneDrive\\바탕 화면\\Pythonworkspace\\*"))

open("test(1).py", "r")
import time
print(time.time())
print(time.localtime())
print(time.asctime())
#time.asctime은 현재 날짜와 시간을 보기 쉽게 나타내줌
#time.strftime은 시간 관련된 것을 세밀하게 표현할 수 있게 도와줌
print(time.strftime("%x", time.localtime(time.time())))

import calendar
print(calendar.calendar(2020))

print(calendar.prmonth(2020, 12))

print(calendar.weekday(2020, 12, 12))

import random
print(random.randint(1, 100))

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

import webbrowser
print(webbrowser.open("https://www.instagram.com/explore/"))