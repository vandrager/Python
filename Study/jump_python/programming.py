
def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result

k = gugu(3)
print(k)

#아래는 나의 풀이
for i in range(1, 1000):
    th = 3
    fi = 5
    result = 0
    i = 1
    while th*i <= 1000:
        result = result + i*th
        i = i + 1
    while fi*i <= 1000:
        result = result + i*fi
        i = i + 1
    while th*fi*i <= 1000:
        result = result - i*fi*th
        i = i + 1
print(result)
#도대체 왜... 뭐가 문제일까ㅠㅠ

#정답 풀이

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)

print(10//3)
print(10%3)

def getTotalPage(m, n):
    if m % n == 0:
        k = m//n
    else:
        k = m//n + 1
    return k

semi = getTotalPage(100, 15)
print(semi)

print(1, 2, 3, sep='\n')

