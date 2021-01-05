import re, os, csv, usecsv

english = "hello. it's me. i am cold. still hungry"
korean = "여보세요. 나야. 차다. 여전히 배고픈"
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
ko_list = re.split('\.', korean)
en_list = re.split('\.', english)

total = []

for i in range(len(en_list)):
    total.append([en_list[i].strip(), ko_list[i].strip()])

usecsv.writecsv('total.csv', total)