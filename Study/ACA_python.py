# menu = ['아메리카노', '카페라떼', '카라멜마끼아또', '카페모카', '프라푸치노']
# price = [3000, 5400, 3200, 4000, 6000]

# ame_menu = menu.index('아메리카노')
# ame_price = price[ame_menu]
# print(ame_price)

# a = list(range(1, 10))
# print(a)

# student_info = {'name': "kale", "age": 20, "height": 180, "weight": 65}
# print(student_info.items())
# print(student_info.keys())
# print(student_info.values())
# print("="*90)
# for (k, v) in student_info.items():
#     print("* {}: {}".format(k, v), end="\n")

# import time
import os
# os.chdir('C://Users//vandr//OneDrive//바탕 화면//Bigdata//Python//Study')
# print(time.time())
# print("2초간 정적이 흘렀다.", time.sleep(0.5))

# data = open('data.txt', 'r', encoding='utf-8')
# datal = data.read()
# print(datal)

# dateline = data.readline()
# print(dateline)

# user_input = input("> 내용을 입력하시오: ")
# datafile = open('data.txt', 'w', encoding='utf-8')
# datafile.write(user_input + '\n')
# datafile = open('data.txt', 'a', encoding='utf-8')
# datafile.write(user_input + '\n')
# datafile = open('data.txt', 'r', encoding='utf-8')
# line = 'init'
# while line:
#     line = datafile.readline()
#     print(line.strip())
os.chdir("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Data/practice")
# import csv
# f = open('전국마을기업표준데이터.csv', 'rt')
# csvread = csv.reader(f)
# print(csvread)

import pandas
import os
import openpyxl

print(os.getcwd())

parking = pandas.read_csv('전국마을기업표준데이터.csv', header=0, encoding= 'euc-kr')
print(parking.head(3))

park_2 = pandas.read_excel('선별진료소_20201226152643.xlsx')
print(park_2.head(3))

parking.to_csv('park.csv')
park_2.to_excel('medic.xlsx')