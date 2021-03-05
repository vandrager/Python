import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")
browser.get('https://www.w3schools.com/html/')
browser.maximize_window()

time.sleep(5)

# 특정 영역까지 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform() # elem이 보이는 곳으로 스크롤을 움직여

# 방법 2 : 좌표 정보 이용
xy = elem.location_once_scrolled_into_view # 함수가 아니니까 () 쓰지 마세요
print("type : ", type(xy))  # dict
print("value : ", xy)



time.sleep(5)
