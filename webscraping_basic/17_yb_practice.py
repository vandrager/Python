import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://google.com")
browser.find_element_by_id("gb_70").click()
elem = browser.find_element_by_id("identifierId")
elem.send_keys("googleid")
elem.send_keys(Keys.ENTER)
pw = browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
pw.send_keys("googlepw")
pw.send_keys(Keys.ENTER)


