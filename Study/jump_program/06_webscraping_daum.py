import requests
from bs4 import BeautifulSoup
url = "https://news.daum.net/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
title = soup.find_all("div", attrs={"class": "item_issue"})
#print(title[0].get_text())

for i in title:
    print(i.get_text().strip())
    print(i.find_all('a')[0].get('href'))


url3 = "https://news.naver.com/"
res = requests.get(url3)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
title = soup.find_all("ul", attrs={"class": "hdline_article_list"})
#print(title[0].get_text())

for i in title:
    print(i.get_text().strip())
    #print(i.find_all('a')[0].get('href'))