import csv, os, usecsv
print(os.getcwd())
os.chdir(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice")
keyword = usecsv.opencsv("2020.12.26_이슈키워드.csv")
print(keyword)
for k in keyword:
    print(k)