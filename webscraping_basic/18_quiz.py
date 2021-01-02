import requests
from bs4 import BeautifulSoup

# 결과물을 파일로 저장하고 싶다면? <출력결과 파일로 저장하기>
import sys
sys.stdout = open('output.txt','w')

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

t1 = soup.find_all("td", attrs={"class": "col1"})
print(t1[0].get_text())

t2 = soup.find_all("td", attrs={"class": "col2"})
t3 = soup.find_all("td", attrs={"class": "col3"})
t4 = soup.find_all("td", attrs={"class": "col4"})
t5 = soup.find_all("td", attrs={"class": "col5"})
total = [t1, t2, t3, t4, t5]
print(t2[0].get_text())

for k in total:
    for j in range(0, 5):
        line = k[j].get_text()
    print(line)

tt = soup.find_all("tr")
print(tt[1].get_text())

for i in range(0, 6):
    print(tt[i].get_text())

for i in range(1, 6):
    print("="*20 + "매물{}".format(i) + "="*20)
    print("거래: ")
    print("면적: ", "(공급/전용)")
    print("가격: ", "(만원)")
    print("동: ")
    print("층: ")
    print("")

total = soup.find("table", attrs={"class": "tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(total):
    column = row.find_all("td")
    # print(row.get_text())
    print("="*20 + "매물{}".format(index+1) + "="*20)
    print("거래: ", column[0].get_text().strip())
    print("면적: ", column[1].get_text().strip(), "(공급/전용)")
    print("가격: ", column[2].get_text().strip(), "(만원)")
    print("동: ", column[3].get_text().strip())
    print("층: ", column[4].get_text().strip())
    print("")

