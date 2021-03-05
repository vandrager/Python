import time
from selenium import webdriver
from selenium.webdriver.common.by import By # elem을 갖고 오는 또 다른 방법!
browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe")

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame("iframeResult") # 프레임 전환을 하겠다. frame id명을 넣어주자
elem = browser.find_element_by_xpath('//*[@id="male"]')
elem.click()

# 선택이 안되어 있으면 선택하기 
if elem.is_selected() == False:
    print("선택 안되어 있으면 선택하기")
    elem.click()
else:
    print("선택 되어있으니까 그냥 넘어감")

elem = browser.find_element(By.XPATH, '//*[@id="female"]')
elem.click()

elem = browser.find_element(By.ID, 'other')
elem.click()

time.sleep(3)