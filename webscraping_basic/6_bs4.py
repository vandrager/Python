import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
# --> <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) #title의 글자만 가져와
# --> 네이버 만화 > 요일별  웹툰 > 전체웹툰
print(soup.a) #soup객체에서 처음 발견되는 a값을 출력
print(soup.a.attrs) #a element가 가지고 있는 속성 정보를 출력
# --> {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"} 
print(soup.a["href"]) #a element의 href 속성 '값' 정보를 출력

print(soup.find('a', attrs={"class": "Nbtn_upload"}))
#find --> 해당하는 첫번째 엘리먼트를 가져옴
#a는 생략가능
print(soup.find(attrs={"class": "Nbtn_upload"}))
print(soup.find(attrs={"title": "여신강림-137화"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
#한 번 해주면 줄바꿈 같은 것 때문에 안나올 수 있음 두 번 넣어주면 정상 출력
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank1.parent)

rank4 = rank1.find_next_sibling("li")
print(rank4.a.get_text())
rank5 = rank3.find_next_sibling("li")
print(rank5.a.get_text())
#하나둘씩 가져오기 귀찮아 죽겠네^^...
print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="사신소년-78화 잠입")
print(webtoon)