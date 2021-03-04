import requests
from bs4 import BeautifulSoup
# 왜 헤더를 넣어야 제대로 나올까? 이 부분은 별도로 학습할 것
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

# url = "https://play.google.com/store/movies/top"
url = "https://www.altools.co.kr/Main/Default.aspx"
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

print(len(movies))

with open("movie.html", "w", encoding="utf8") as f:
    f.write(res.text)
    f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)