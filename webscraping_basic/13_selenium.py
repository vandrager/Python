# 셀레니움 웹페이지 텍스트 자동화 가능한 유명한 프레임워크
# chrome://version/에서 나의 구글 버전 확인
# webdriver? 크롬용, 익스플로어용 등 다양하게 존재
# chromedriver 구글 검색 웹사이트 접속
# chrome 버전과 win/mac 타입에 맞게 설치
# 단순 파이썬 파일로 실행하면 자동 종료되고 파이썬 터미널 또는 주피터 노트북 파일로 실행하면 자동 종료되지 않는다.
# 크롬 브라우저/셀리니움 업데이트 다 해보았고 webdriver 문제도 아니었음, Firefox도 안돼
from selenium import webdriver

#나는 python 폴더 외부에 크롬 드라이버가 있기 때문에 파일경로 입력 필요, 만약 내부에 있다면 입력 필요X
browser = webdriver.Chrome("C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/chromedriver.exe")

#1. 네이버 이동
browser.get("http://naver.com")

#2. 로그인 버튼 클릭 
elem = browser.find_element_by_class_name("link_login")
elem.click()

#(selenium 기능 학습)
# browser.back()
# browser.forward()
# browser.refresh()
# elem = browser.find_element_by_id("query")
# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_tag_name("a") ( 하나만 )
# elem = browser.find_elements_by_tag_name("a") ( 모두다 )
# for e in elem:
#     e.get_attribute("href")
# browser.get("http://daum.net")
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# elem.click()
# browser.quit() #아예 꺼버리기
# browser.close() #탭만 닫아버리기
# # 터미널에 위와 동일 내용 입력


#3. id, password 입력

