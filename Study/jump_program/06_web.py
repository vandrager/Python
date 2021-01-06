import os, re, usecsv
import requests
from bs4 import BeautifulSoup as bs
import urllib.request as ur
url = "https://quotes.toscrape.com/"

res = requests.get(url)
soup = bs(res.text, "lxml")
all_list = soup.find_all("div", attrs={"class": "quote"})
for a in all_list:
    print(a.text)
url2 = "https://news.daum.net/"
res = requests.get(url2)
soup = bs(res.text, "lxml")
headline = soup.find_all("div", {'class': 'item_issue'})

for i in headline:
    print(i.text, i.find_all('a')[0].get('href'))
    soup3 = bs(ur.urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
    for j in soup3.find_all('p'):
        j.text