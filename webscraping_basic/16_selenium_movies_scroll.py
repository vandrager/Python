from selenium import webdriver
browser = webdriver.Chrome("chromedriver.exe")
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # 1920 x 1080
# browser.execute_script("window.scrollTo(0, 2080)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")
# page_source로 스크롤 끝까지 내렸을 때의 html 정보를 가져오게 됨

# 정보) 속성을 리스트로 감싸주어 조건을 만족하는 모든 데이터를 가져올 수 있다.
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})
print(len(movies))


for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
     # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link

    # 할인 전 가격
    # #1번과 #2번을 분리하지 않으면 null값을 가져와서 오류가 발생하므로 분리해야함
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"}) #1번
    if original_price: #2번
        original_price = original_price.get_text()
    else:
        print(f"제목 : {title}")
        print(f"금액 : {price}")
        print(f"링크 : https://play.google.com{link}")
        print("-" * 100)
        continue

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print(f"링크 : https://play.google.com{link}")
    print("-" * 100)

#f-strings (최근 가장 인기)
# 앞에 f 를 붙이고 {변수명} 형태로 작성한다. (대문자 F 도 가능)
# 만약 내가 할인 전/후 금액 다 있는거 말고 할인 후 금액만 있는 것도 출력하고 싶다면 어떻게 해야할까?
# 간단하게 if else 문 뒤에 결과를 입력하면 된다. continue하면 바로 다음 movie로 넘어가기 때문에 if 문에서 print출력하면 깔꼼하게 출력 한다.
