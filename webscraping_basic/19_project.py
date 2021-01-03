from selenium import webdriver
browser = webdriver.Chrome(r"C:\Users\vandr\OneDrive\바탕 화면\Bigdata\Python\webscraping_basic/chromedriver.exe")


url = "http://www.naver.com"
browser.get(url)
browser.find_element_by_class_name("input_text").send_keys("오늘 수원 날씨")
browser.find_element_by_class_name("ico_search_submit").click()
weather = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[1]/p")
print("[오늘의 날씨]")
print(weather.text)
now_w = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/p/span[1]")
now_h = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[1]/span[3]/span")
now_l = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/ul/li[2]/span[1]/span[1]/span")
print(f"현재 {now_w.text}도 (최저 {now_l.text}도/최고 {now_h.text}도)")
rain_up = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[7]/ul[1]/li[1]/span[2]/span[2]/span[2]")
rain_down = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[7]/ul[1]/li[1]/span[3]/span[2]/span[2]")
print(f"오전 강수확률 {rain_up.text}% / 오후 강수확률 {rain_down.text}%")
print("")
mise = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/dl/dd[1]/span[1]")
chomise = browser.find_element_by_xpath("//*[@id='main_pack']/section[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div/dl/dd[2]/span[1]")
print("미세먼지 {}".format(mise.text))
print("초미세먼지 {}".format(chomise.text))
# 보통이나 좋음 같은 것은 어떻게 가져오지..?

url2 = "https://news.naver.com/"
browser.get(url2)
head = browser.find_elements_by_xpath("//*[@id='today_main_news']/div[2]/ul/li[1]/div[1]/a")
                                       #//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a
#print(browser.find_element_by_xpath("//*[@id='today_main_news']/div[2]/ul/li[1]/div[1]/a").get_attribute("href"))
#nowText = browser.find_element_by_class_name("hdline_article_tit").get_attribute("href")
#print(nowText)
# for i in range(1, 4):
#     print("{}.".format(i), browser.find_element_by_xpath("//*[@id='today_main_news']/div[2]/ul/li[i]/div[1]/a").text)
#     print("(링크: {})".format(browser.find_element_by_xpath("//*[@id='today_main_news']/div[2]/ul/li[i]/div[1]/a").get_attribute("href")))
    

# for index, i in enumerate(head):
#     print(f"{index+1}. {i.div.text}")
#     print(link + i["href"])
#     if index == 2:
#         break



# for i in range(1, 4):
#     print(i, ".", head[i].text)
#     print(head[i].find("a")["href"])