print("hello")
import csv
import requests
from bs4 import BeautifulSoup


url = "https://kr.noxinfluencer.com/2020-top-influencers-youtube-subs-kr"
filename = "youtube100.csv"
f = open(filename, "w", encoding="euc-kr", newline="") #new라인이 없으면 줄마다 한 칸씩 공백이 발생
writer = csv.writer(f)
title = "순위    유튜브 채널    구독자   구독자 증가".split("\t")    
writer.writerow(title)

res = requests.get(url)
# res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
data_rows = soup.find("div", attrs={"class": "list-content common"}).find_all("href")
print(data_rows[0].get_text())
# for row in data_rows:
#     columns = row.find_all("td")
#     if len(columns) <= 1: #의미없는 데이터는 skip
#         continue
#     data = [column.get_text().strip() for column in columns]
#     print(data)
#     writer.writerow(data)

#     print(data[0])