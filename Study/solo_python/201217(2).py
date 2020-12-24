key = ["name", "hp", "mp", "level"]
val = ["기사", 200, 30, 5]
chr = {}

t = 0
for i in key:
    chr[i] = val[t]
    t += 1

print(chr)

limit = 10000
i = 1

sum_value = 0
while sum_value < limit:
    sum_value = sum_value + i
    i = i + 1

print(i, sum_value)

max = 0
a = 0
b = 0

for i in range(1, 100//2 + 1):
    j = 100 - i
print(i, j)
c = i*j
if max < c:
    a = i
    b = j
    max = c
print(max)

print(list(range(0, 10, 3)))

ar = [270, 324, 334, 34, 25]
for i in range(len(ar)):
    print("{}, {}번째 반복입니다.".format(ar[i], i))

for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))

while True:
    print(".", end= " ")
    print("")
    break

import time
num = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    num += 1

print("5초 동안 {}번 반복했습니다.".format(num))

def mul(*values):
    out = 1
    for i in values:
        out *= i
    return out

print(mul(2, 4, 5, 6))
        


print(mul(1, 2, 3, 4))


def fun(value=10)