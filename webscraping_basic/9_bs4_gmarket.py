# HTTP
# GET 어떤 내용을 누구나 볼 수 있게 URL에 포함하여 전송
# --> https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user
# POST URL이 아닌 바디에 숨겨서 전송
# 쿠팡은 접속이 안되는 현상이 발생하여 bgf retail 홈페이지로 실습
import requests
from bs4 import BeautifulSoup

url = "https://browse.gmarket.co.kr/search?keyword=%EC%A1%B0%EB%A6%BDpc"
res = requests.get(url)


soup = BeautifulSoup(res.text, "lxml")

pc = soup.find_all("span", attrs={"class": "text__item"})
print(len(pc))
out = []
for i in pc:
    out.append(i.get_text())
print(out)

for v in out:
    print("*", v)
    print("="*100)