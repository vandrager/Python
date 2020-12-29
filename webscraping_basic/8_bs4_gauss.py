import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

gauss = soup.find_all("td", attrs={"class": "title"})
link = gauss[0].a["href"]
print("https://comic.naver.com" + link)

#만화제목과 링크 가져오기
# for g in gauss:
#     title = g.get_text()
#     link = "https://comic.naver.com" + g.a["href"]
#     print(title, link)

#평점 구하기
rating = soup.find_all("div", attrs={"class": "rating_type"})
for i in range(10):
    out = 0
    for g in rating:
        record = float(g.find("strong").get_text())
        out += record
        print(record)
    print(out/len(rating))

output = 0
for g in rating:
    rate = g.find("strong").get_text()
    print(rate)
    output += float(rate)

print("전체 점수: ", output)
print("평균 점수: ", output/len(rating))