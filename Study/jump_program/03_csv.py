import csv, os
f = open('a.csv', 'r', encoding='utf-8')

k = csv.reader(f)
for i in k:
    print(i)

a_list = []
f.seek(0) #커서를 처음(0)으로 이동해야함 csv.reader(f) 때문에 커서가 맨 마지막으로 이동했기 때문
for i in k:
    print(i)
    a_list.append(i)

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

print(opencsv('b.csv'))

def writecsv(filename, the_list):
    with open(filename, 'w', newline="") as f:
        a = csv.writer(f, delimiter = ",")
        a.writerows(the_list)
        

os.getcwd(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")
keyword = opencsv("2020.12.26_이슈키워드.csv")
print(keyword)