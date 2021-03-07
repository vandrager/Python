import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")
browser.maximize_window()



# browser.find_element_by_xpath('//*[@id="identifierId"]').click()
# browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys("vandrager21@gmail.com") # 브랜드 이름도 자동화
# browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(Keys.ENTER)

# 스택 오버플로우 경유해서 구글 로그인 (21.03.07 기준 막힘)
browser.get('https://stackoverflow.com/')
time.sleep(0.5)
browser.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()
time.sleep(0.5)
browser.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
time.sleep(0.5)
browser.find_element_by_id('identifierId').send_keys('아이디')
browser.find_element_by_xpath( '//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(2)
browser.find_element_by_xpath( '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('비밀번호')
browser.find_element_by_xpath( '//*[@id="passwordNext"]/div/button/div[2]').click()
time.sleep(2)
browser.get('https://analytics.google.com/analytics/web/#/p257223633/reports/defaulthome?params=_u..nav%3Ddefault')
time.sleep(2)
