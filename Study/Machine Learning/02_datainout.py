import os, re, requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import urllib.request as ur
os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
# csv 데이터 불러오기
apt = pd.read_csv('wantapt.csv', encoding= 'euc-kr')
# 헤더값은 기본으로 0 1행이면 header=1 이케 수정, 행없으면 header=none
dd = apt.head()
print(apt.head())
dd.to_csv("appt.csv", encoding = "euc-kr")

# excel 데이터 불러오기
# pop = pd.read_excel('Floating_population_2011.xlsx')
# print(pop[:5])

# json 파일 불러오기
jj = pd.read_json("read_json_sample.json")

jj.set_index('name')
print(jj)
jj.to_json("module_sample.json")

html = pd.read_html("sample.html")
print(html)

url = r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice\sample.html'
tables = pd.read_html(url)
print(len(tables))

for i in range(0, 2):
    print(f"table{i}")
    print(tables[i], '\n')

df = tables[1]

df.set_index(['name'], inplace=True)
print(df)

# 책 저자 분이 도대체 왜 이렇게 만드신건지 의문... 심지어 안돼
# url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
# resp = requests.get(url)
# soup = bs(resp.text, 'lxml')
# rows = soup.select('div > ul > li')
# etfs = {}
# for row in rows:
#     try:
#         etf_name = re.findall('^(.*) \ (NYSE)', row.text)
#         etf_market = re.findall('\((.*)\|', row.text)
#         etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)

#         if (len(etf_ticker) > 0) & (len(etf_market) > 0):
#             etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]
#     except AttributeError as err:
#         pass

# print(etfs)

# api_key = ''
# import googlemaps
# maps = googlemaps.Client(key=api_key)
# lat = []
# lng = []
# places = ["서울시청", "국립국악원", "해운대해수욕장"]
# i = 0

# for place in places:
#     i = i + 1
#     try:
#         print(i, place)
#         geo_location = maps.geocode(place)[0].get('geometry')
#         lat.append(geo_location['location']['lat'])
#         lng.append(geo_location['location']['lng'])

#     except:
#         lat.append("")
#         lng.append("")
#         print(i)

# df = pd.DataFrame({"위도": lat, "경도": lng}, index=places)
# print(lng, lat)
# print(df)

medi = pd.read_excel("medic.xlsx")
print(medi)
medi_top10 = medi.head(10)
medi_top10.to_excel("top10.xlsx")

#여러 개의 데이터 프레임을 하나의 EXCEL 파일로 저장
df1 = pd.DataFrame([['jerry', 'ben', 'oken'],
                    ['A', 'B', 'A'],
                    ['B', 'C', 'A'],
                    ['A', 'A', 'B']],
                    columns=["name", "english", "spear"])
df1.set_index('name')
df2 = pd.DataFrame([[1, 2, 3, 4],
                    [3, 4, 5, 6],
                    [1, 2, 3, 4],
                    [1, 2, 3, 6]],
                    columns=["name", "english", "spear", "hello"])
df2.set_index('name')

writer = pd.ExcelWriter("excelwrite.xlsx")
df1.to_excel(writer, sheet_name="df1")
df2.to_excel(writer, sheet_name="df2")
writer.save()


