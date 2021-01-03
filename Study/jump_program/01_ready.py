# Chapter 01 ~ 02 연습문제 풀이
print("hello, python")

if 3 in range(5):
    print('there is 3')


for i in range(10):
    print(i, end="\t")

print("")
print(14 // 4)
print(14 % 4)
print(round(1.12345, 2))
a = int(input("나이를 입력하세요: "))
print(40-a)

plus = lambda x, y: x + y
print(plus(34, 54))
def mean_middle(a, b):
    return int((a+b)/2)

print(mean_middle(10, 4))
print(10 - mean_middle(10, 4))

b = list(range(1, 15))
print(b)
for i in b:
    if i >= 10:
        print(i-10)
    else:
        print(i)
