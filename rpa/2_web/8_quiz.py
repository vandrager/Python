import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")
browser.maximize_window()
browser.get('https://www.w3schools.com')

elem = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div[1]/a[1]')
elem.click()

elem = browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]')
elem.click()

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]')
elem.click()



elem = browser.find_element_by_xpath('//*[@id="fname"]')
elem.send_keys("나도")


elem = browser.find_element_by_xpath('//*[@id="lname"]')
elem.send_keys("코딩")

elem = browser.find_element_by_xpath('//*[@id="country"]')
elem.send_keys("Canada")

elem = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
elem.send_keys("퀴즈 완료하였습니다.")

time.sleep(5)

elem = browser.find_element_by_xpath('//*[@id="main"]/div[3]/a')
elem.click()

browser.quit()
