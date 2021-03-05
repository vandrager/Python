import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame("iframeResult") # 프레임 전환을 하겠다. frame id명을 넣어주자
elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem.click()
elem = browser.find_element_by_xpath('//*[@id="vehicle2"]')
elem.click()
elem = browser.find_element_by_xpath('//*[@id="vehicle3"]')
elem.click()