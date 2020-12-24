def print_k(n=2, *value):
    for i in range(n):
        for v in value:
            print(v)
            print("")
        


print_k(2, "오하이오")

def sum(s, e, step =1):
    out = 0
    for i in range(s, e+1, step):
        out += i
    return print(out)

sum(0, 100, 10)

def mum(*values):
    out = 1
    for i in values:
        out = out * i
    return print(out)

mum(5, 7, 9, 10)

def fac(n):
    out = 1
    for i in range(1, n+1):
        out *= i
    return out

print(fac(5))

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

print(fib(5))

count = 0
def fib2(n):
    print("fibonacci({})를 구합니다.".format(n))
    global count
    count += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)

a = fib2(3)
print("{} 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(a, count))

diction = {
    1:1,
    2:2

}

def fib3(n):
    if n in diction:
        return diction[n]
    else:
        out = fib3(n-1) + fib3(n-2)
        diction[n] = out
        return out



exam = [[1,2,3], [4, [5, 6]], 7, [8, 9]]
print(type(exam[2]))
print(type(exam[0][0]))
print(type(exam[1][1]))
test = [1, 2, 3]
exam += test
print(exam)
#재귀함수 너무 어렵다... 바로 이해가 안돼 이건 강의 진짜 들어야할 듯ㅠ0ㅠ

#그냥 풀어버린다면?
def flat(data):
    output = []
    for i in data:
        if type(i) == int:
            output.append(i)
        if type(i) == list:
            for j in i:
                if type(j) == int:
                    output.append(j)
                if type(j) == list:
                    output.extend(j)
    return output

#재귀함수로 효율적으로 만들면?
def flation(data):
    output = []
    for i in data:
        if type(i) == list:
            output += flation(i)
        else:
            output.append(i)
    return output
print(flat(exam))
print(flation(exam))


#난이도 최상.. 이건 도대체 뭐하라는건지 모르겠음
anmin = 2
anmax = 10
full = 100
memo = {}

def test(still, sit):
    key = str([still, sit])
    if key in memo:
        return memo[key]
    if still < 0:
        return 0
    if still == 0:
        return 1
    count = 0
    for i in range(sit, anmax+1):
        count += test(still-i, i)
    memo[key] = count
    return count

print(test(full, anmin))

po = 1, 2
print(type(po))
[mino, pp] = [180, 185]
print(type(mino))

power = lambda x: x*x
under_3 = lambda x: x<3

a = [1, 2, 3, 4, 5]
out_a = map(power, a)
out_b = filter(under_3, a)
print(list(out_a))
print(list(out_b))

out_c = map(lambda x: x**3, a)
out_d = filter(lambda x: x<4, a)
print(list(out_c))
print(list(out_d))

file = open("basci.txt", 'w')
file.write("hello i am yong beom")
file.close()

with open("basci.txt", 'r') as file:
    contents = file.read()

print(contents)

import random

hangul = list("가나다라마바사아자차카타파하")

with open("info.txt", 'w') as file:
    for i in range(1000):
        name = random.choice(hangul) + random.choice(hangul)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write("{}, {}, {}\n".format(name, weight, height))

with open("info.txt", 'r') as pd:
    for line in pd:
        (name, weight, height) = line.strip().split(", ")
    
    bmi = int(weight) / ((int(height) / 100)**2)
    result = ""
    if 25 <= bmi:
        result = "과체중"
    elif 18.5 <= bmi:
        result = "정상 체중"
    else:
        result = "저체중"
    print('\n'.join([
        "이름: {}",
        "몸무게: {}",
        "키: {}",
        "BMI: {}",
        "결과: {}"
    ]).format(name, weight, height, bmi, result))
    print()

   # if (not name) or (not weight) or (not height):
        #continue
#continue에서 에러가 뜸;;

#오, 아래껀 좀 꿀팁인듯 map쓰면 1::2::3::4::5::6 이케 만들 수 있음
number = [1, 2, 3, 4, 5, 6]
print("::".join(map(str, number)))

nb = list(range(1, 11))
print("#홀수만 추출하기")
print(list(filter(lambda x: x % 2 != 0, nb)))
print(list(filter(lambda x: x % 2 == 0, nb)))
print(list(filter(lambda x: 3 <= x < 7, nb)))
print(list(filter(lambda x: x**2 < 50, nb)))