result = 0
def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(4))

result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))

class calculator:
    def __init__(self):
        self.result = 0

    def adder(self,num):
        self.result += num
        return self.result

cal1 = calculator()
cal2 = calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

class service:
    secret = "영구는 배꼽이 두 개다."
    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s입니다." %(a, b, result))

peny = service()
peny.sum(1, 2)

class service:
    secret = "용범이는 미래에 반드시 성공한다."
    def setname(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("\"%s님 %s + %s = %s입니다.\"" %(self.name, a, b, result))

wet = service()
wet.setname("Coca cola")
wet.sum(10, 20)

class service:
    secret = "용범이는 미래에 반드시 성공한다."
    def __init__(self, name):
        self.name = name
    def sum(self, a, b):
        result = a + b
        print("\"%s님 %s + %s = %s입니다.\"" %(self.name, a, b, result))

#__init__을 넣었더니 엥 필수가 되어버렸잖앙?

king = service("박용범")
king.sum(7, 42)

#사칙연산 클래스 만들기
class fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    print(result)

a = fourcal()
a.setdata(1, 2)
print(a.sub())

class housepark:
    lastname = "박"
    def setname(self, name):
        self.fullname = self.lastname + name

foll = housepark()
foll.setname("제구")
print(foll.fullname)
    
class housepark:
    lastname = "박"
    def setname(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s로 여행을 가다."%(self.fullname, where))

toy = housepark()
toy.setname("칼린")
toy.travel("언더월드")

class housepark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s로 여행을 가다."%(self.fullname, where))
    def love(self, other):
        print("%s, %s와 사랑에 빠졌네" %(self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s와 결혼했네~ 경사났네~ 얼씨구나~" %(self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s와 격렬하게 다투고 뒤집고 난리났네" %(self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s와 이혼했네~ 옹헤야~ 슬프구나~" %(self.fullname, other.fullname))

mime = housepark("폭풍")
mime.travel("테이스티월드")

class housekim(housepark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행을 %d일 가네"%(self.fullname, where, day))

judy = housekim("독도")
judy.travel("부싼", 3)

#클래스 상속 개쩌네... ㄷㄷ #상속이 나라고 미래다.

peter = housepark("범석")
jenny = housekim("수지")
peter.love(jenny)
peter + jenny

# __init__, __add__ 함수 유용하네 잘 알아두자

peter.fight(jenny)
peter - jenny

peter.travel("부산")
jenny.travel("부산", 3)
peter.love(jenny)
peter + jenny
peter.fight(jenny)
peter - jenny

import mod
print(mod.sum(20, 30))

import mod
print(mod.safe_sum(20, 'k'))

from mod import sum, safe_sum
#from mod import sum, safe_sum == from mod import * (*은 모든 것이라는 뜻, 즉 모든 함수를 불러오라는 명령)
print(sum(1, 2))

print(safe_sum(10, 15))