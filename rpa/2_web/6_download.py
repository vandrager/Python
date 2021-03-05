import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 파일 다운로드 옵션 설정, 경로 변경
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\vandr\OneDrive\바탕 화면\Bigdata'})

browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\chromedriver.exe", options=chrome_options) # 옵션 추가
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')
browser.maximize_window()

browser.switch_to.frame("iframeResult")
elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()