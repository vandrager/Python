def sum(a, b):
    result = a + b
    return result

a = 3
b = 4
c = sum(a, b)
print(c)

k = 7
i = 8
w = sum(k, i)
print(w)


def say():
    return 'hi'

a = say()
print(a)

def sum(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

a = 8
b = 5
sum(a,b)
print(sum(a, b))

#def sum_many(*args):
    #sum = 0
    #for i in args:
        #sum = sum + i
   # return sum

def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)
result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다."%nick)

say_nick("야호")
say_nick("바보")

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다."%name)
    print("나의 나이는 %d살입니다."%old)
    if man:
        print("\"남자입니다.\"")
    else:
        print("여자입니다.")
#old와 True 인수 위치를 변경하면 오류 발생, 인터프리터가 어디에 대입할지를 이해 몬함
say_myself('박용범', 26, True)


a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

a = input("숫자를 입력해주세요: ")
print(a)
number = input("숫자를 입력하세요: ")
print(number)

print("life", "is","too", "short")

for i in range(10):
    print(i, end=" ")
    print("")

f = open("새파일.txt", 'w')
f.close()