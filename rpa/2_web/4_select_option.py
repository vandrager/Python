import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame("iframeResult") # 프레임 전환을 하겠다. frame id명을 넣어주자
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# option[1] # 첫 번째 항목
# option[2] # 두 번째 항목
# option[3] # 세 번째 항목
# option[4] # 네 번째 항목
# ...

elem.click()
time.sleep(3)

# 텍스트 값을 통해서 선택하는 방법
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Saab"]')
elem.click()
time.sleep(3)

# 텍스트 값이 부분 일치하는 항목을 선택하는 방법
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()
time.sleep(3)