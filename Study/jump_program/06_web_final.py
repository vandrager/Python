import os, re, usecsv
import requests
from bs4 import BeautifulSoup as bs
import urllib.request as ur
url = "https://news.daum.net/"
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, 'lxml')
# title = soup.find_all("div", attrs={"class": "item_issue"})
#print(title[0].get_text())

# for i in title:
#     print(i.get_text().strip(), i.find_all('a')[0].get('href'))

os.chdir(r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Data\practice')
f = open("links.txt", 'w')
for i in soup.find_all('div', {"class": "item_issue"}):
    f.write(i.find_all('a')[0].get('href') + '\n')

f.close()

article = "https://news.v.daum.net/v/20210106171745306"
soup = bs(ur.urlopen(article).read(), 'html.parser')
f = open('article1.txt', 'w')
for i in soup.find_all('p'):
    f.write(i.text)
f.close()

# soup 부분에서 res.text보다  ur.urlopen(링크), 'html.parser' 방식이 더 긁어오는게 많은 것 같음!
url = "https://news.daum.net/"
soup = bs(ur.urlopen(url).read(), 'html.parser')
f = open('article_total.txt', 'w')
for i in soup.find_all('div', {'class': "item_issue"}):
    try:
        f.write(i.text + '\n')
        f.write(i.find_all('a')[0].get('href') + '\n')
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
        for j in soup2.find_all('p'):
            f.write(j.text)
    except:
        pass

f.close()

# 웹크롤링 실행 파일 만들기
# 아래 명령프롬프트 창 터미널에서
# pyinstaller --onefile ['파이썬 파일명'].py
# pyinstaller --onefile article_collecter.py
# 작업 폴더에 dits폴더 생성 들어가면 실행파일이 생겼다는 것을 확인 가능