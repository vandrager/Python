m = 5000

if m <= 3000:
    print("\"전동킥보드를 타고 가라.\"")
else:
    print("\"걸어가라 닝겐\"")

x = 3
y = 2
print(x > y)

kale = "man"
cash = 100000000

if kale == "woman" or cash >= 1000000:
    print("yes")
else:
    print("get out fucker")

if not kale == "man":
    print("yes")
else:
    print("no")

print('d' in ['a', 'b', 'c'])

pk = ['paper', 'cellphone']
card = 1

if 'money' in pk:
    print("\"택시를 타고 가자\"")
else:
    if card:
        print("\"좋아, 택시를 탈 수 있드아\"")
    else:
        print("... 걸어가자.")

if 'money' in pk:
    print("\"택시를 타고 가자\"")
elif card:
    print("쪼아, 택시를 탈 수 있따!")
else:
    print("이게 도대체 뭔 차이야...")

treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d 번 찍었습니다." %treehit)
    if treehit == 10:
        print("\"나무 넘어가유~\"")

prompt = """
1. add
2. del
3. list
4. quit
"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 1

while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈이 부족합니다. 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." %coffee)
    if coffee < 1:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10:
    a = a+1
    if a % 2 == 0: continue
    print(a)

#무한루프 만들기(걸리면 멘붕)
# while True:
    #print("ctrl + c를 눌러야 while문을 빠져나갈 수 있습니다.")

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

exam = [90, 25, 67, 45, 80]
number = 0
for mark in exam:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다. 축축축~~" %number)
    else:
        print("%d번 학생은 불합격입니다. 흑흑흑~~" %number)

a = range(11)
print(a)
sum = 0
for i in a:
    sum = sum + i
print(sum)

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print("")

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2, 10)
for y in range(1, 10)]
print(result, end = " ")

