pin = "881120-1068234"
yymmdd = "19" + pin[0:6]
num = pin[7:]
print(yymmdd)
print(num)

print(pin[7])
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

a = ['life','is','too','short']
result = a[0] + " " + a[1] + " " + a[2] + " " + a[3]
print(result)

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = aSet
print(b)
a = (1, 2, 3)


a = {'a':90, 'b':80, 'c':70}
result = a['b']
a.pop('b')
print(a)
print(result)

a = b = [1, 2, 3]
b = a[:]
a[1] = 4
print(b)
print(a)
"""
아래는 내가 못풀었던 문제들
"""

a = ['life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
#join은 a라는 문자열의 각각의 문자 사이에 " "라는 공백을 삽입해준다.
#아래와 같이 변형할 수 있으니 참고참고

km = ['time', 'is', 'now', 'what']
km = "   ".join(km)

print(result)

a = (1, 2, 3)
a = a + (4,)
print(a)
#튜플은 추가할 때 ()괄호 넣고 속성값 옆에 ,도 같이 넣어주자