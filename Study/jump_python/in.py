f = open("새파일.txt", 'w')
f.close()
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

#while True:
#line = f.readline()
    #if not line: break
    #print(line)
#f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("새파일.txt", 'a')
for i in range(11, 21):
    data = "%d번째 줄입니다.\n"%i
    f.write(data)
f.close()