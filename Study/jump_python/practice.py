print(5)
print(-10)
print(1000)
print(5+3)
print(10*3)
print("이제 일해라 용범아!!")
print("Good night bro")
print("Fighting, bro!")
a = 4.5e-10
print(a)
print(a*1000000000)
k = 2**10
print(k)
b = 10
print(k/b)
print(7/4)
print(7//4)
print(7%3)
print(5%3)
food = "python's favorite food is perl"
print(food)
beer = "\"life is good, and park's car is nice!\" he says."
print(beer)
multi = """
\"life is too short
you need python\"
"""
print(multi)

hey = """
\t fire
is
dangerous
"""
print(hey)
head = "python"
tail = " is amazing"
print(head + tail)
print(head*3)

print("="*50)
print("park yong beom is fantastic")
print("="*50)
print(head[-1])
print(food[0:6])
print(food[0:])

a = "20201207rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
a = a[:8] + "sunny"
print(a)

go = "i eat %d pizza" %3
print(go)
now = "eat some %s chicken stick" % "five"
print(now)
come = "hungry, %d hungry very very" % k
print(come)
ptom = "tonight is very hot %d%% like pizza and chicken %s" %(k, food)
print(ptom)
print("\"have a good night guy!\"")
print("%10sjane" %'hi')
print("%-10sjane" %'hi')
print("%0.4f" % 3.42134234)
a = "hobby"
print(a.count("b"))
print(a.find("o"))
print(a.find("k"))
a = ","
print(a.join('abcd'))
print(a)
u = a.join('abcd')
print(u)
t = "   hi   "
print(u.upper())
l = u.upper()
print(l)
print(l.lower())
print(t)
print(t.lstrip())
print(t.strip())
a = "Life is too short"
print(a.replace("Life", "Time"))
print(a)
print(u)
print(u.split(","))
print(a.split())

a = "love me"
b = "love yourself"
c = "don't be sad"
print("i wanna be {0} star and {1} and {2}".format(a,b,c))
print("\"{pizza} and {beer} are my best combination food\"".format(pizza = "8282", beer = "1592"))
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:=^10}".format("hi"))

e = [1, 2, 3, [[2, 3], 5]]
print(e[3][0][1]+ e[1])
a = [1, 2, 3, [1, 2, 3], 4, 5]
print(a[3][:3])
b = [1, 2, 3]
c = [4, 5, 6]
d = b + c
print(d)
tu = b*3
print(tu)
pu = b[2]*"hi"
print(pu)
c[1:2] = ["b", "u", "r"]
print(c)
c[1:4] = []
print(c)
del c[1]
print(c)
c.append(8)
c[2:4] = [5, 6]
print(c)
c.sort()
print(c)
c.insert(0, 3)
print(c)
print(b)
d = c + b + [7, 9]
d.sort()
d.remove(3)
print(d)
W = (1)
print(W)
q = [1, 2, "a", "b"]
print(q)
t1 = (1, 2, 'a', 'b')
print(t1)
t2 = 3, 4
print(t1 + t2)
print(t2*3)

dic = {'name':'pay', 'skill':'design','food':'pizza'}
print(dic)
del dic['name']
print(dic)
grade = {'yong':171, 'beom':170}
print(grade['yong'])
"""
this is me
"""
print("="*50)
dic["name"] = 'pay'
print(dic.keys())
print(dic.values())
wk = list(dic.values())
print(wk)
s1 = set([1, 2, 3,])
print(s1)
s2 = set('hello')
print(s2)
s3 = set([1, 2, 3, 4, 5, 6, 7, 8])
s4 = set([1, 3, 4, 5, 6, 8, 0])
print(s3 & s4)
print(s3 | s4)
print(s3 - s4)

s4.add(12)
print(s4)
s4.update([11, 13, 14])
print(s4)
s4.remove(11)
print(s4)

l1 = [1, 2, 3, 4]
l1.remove(3)
print(l1)
l1[1:] = []
print(l1)

a = [1, 2, 3, 4]
while a:
    a.pop()
    print(a)

if []:
    print("true")
else:
    print("false")

if [1, 2, 3]:
    print("true")
else:
    print("false")

del(a)

v = [1, 2, 3]
k = [4, 5, 6]
g = k[:]
k[1] = 9
print(k)
print(g)
