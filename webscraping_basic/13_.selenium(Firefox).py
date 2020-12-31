from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:/Users/vandr/OneDrive/바탕 화면/Bigdata/Python/webscraping_basic/geckodriver.exe')

driver.get("https://www.google.com/")
driver.find_element_by_xpath
driver.implicitly_wait(10)