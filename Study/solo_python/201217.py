#append는 리스트 맨 끝에 추가하기
#insert는 지정된 중간 자리에 값을 추가하기

list = [1, 2, 3, 4]
list.append(5)
list.insert(0, 2)
list[1] = 2
list.pop()
list.remove(4)
list.extend(list)
del list[3]
list.clear()
list = [1, 2, 3, 3, 4]
print(list)

for i in range(100):
    print("가즈아~~")

lol = [[1, 2, 3], [4, 5, 6, 7], [8, 9],]
for i in lol:
    for k in i:
        print(" -", k)

#아래는 두 번 연속 못풀었던 문제 풀이보니깐 쉽네ㅋ,,,
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
out = [[], [], []]
print(len(out))
for i in num:
    out[(i+2) % 3].append(i)
print(out)

pet = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]

print("#우리 동네 애완 동물들")
for i in pet:
    print("{} {}살".format(i["name"], i["age"]))

print(pet[0].keys())

num = [1, 2, 3, 4, 5, 6, 1, 2, 3, 5, 1, 3, 5, 6]
count = {}
for n in num:
    if n not in count:
        count[n] = num.count(n)

print(count)